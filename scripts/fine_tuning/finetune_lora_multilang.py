#!/usr/bin/env python3
import argparse
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import torch


def tokenize_fn(example, tokenizer, max_length):
    text = example["prompt"] + " " + example["completion"]
    out = tokenizer(
        text,
        truncation=True,
        max_length=max_length,
        padding="max_length",
    )
    out["labels"] = out["input_ids"].copy()
    return out


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", required=True)
    parser.add_argument("--valid", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--max-length", type=int, default=1024)

    parser.add_argument("--per-device-train-batch-size", type=int, default=2)
    parser.add_argument("--per-device-eval-batch-size", type=int, default=2)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--num-train-epochs", type=float, default=2.0)
    parser.add_argument("--warmup-ratio", type=float, default=0.03)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--logging-steps", type=int, default=10)

    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--lora-dropout", type=float, default=0.05)

    parser.add_argument(
        "--target-modules",
        nargs="+",
        default=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj"
        ],
    )

    parser.add_argument("--load-in-4bit", action="store_true", default=True)
    parser.add_argument("--no-load-in-4bit", dest="load_in_4bit", action="store_false")
    return parser.parse_args()


def main():
    args = parse_args()

    print(f"Loading tokenizer for {args.model_name} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Loading datasets ...")
    train_ds = load_dataset("json", data_files=args.train)["train"]
    valid_ds = load_dataset("json", data_files=args.valid)["train"]

    print("Tokenizing train dataset ...")
    train_ds = train_ds.map(
        lambda x: tokenize_fn(x, tokenizer, args.max_length),
        remove_columns=train_ds.column_names,
    )
    print("Tokenizing valid dataset ...")
    valid_ds = valid_ds.map(
        lambda x: tokenize_fn(x, tokenizer, args.max_length),
        remove_columns=valid_ds.column_names,
    )

    quantization_config = None
    if args.load_in_4bit:
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )

    print(f"Loading base model for {args.model_name} ...")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        quantization_config=quantization_config,
        device_map="auto",
        torch_dtype=torch.float16,
        trust_remote_code=True,
    )

    if args.load_in_4bit:
        model = prepare_model_for_kbit_training(model)

    print("Applying LoRA ...")
    peft_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=args.target_modules,
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.per_device_train_batch_size,
        per_device_eval_batch_size=args.per_device_eval_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        num_train_epochs=args.num_train_epochs,
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        logging_steps=args.logging_steps,
        eval_strategy="epoch",
        save_strategy="epoch",
        fp16=True,
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=valid_ds,
        data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
    )

    print("Starting training ...")
    trainer.train()
    print("Saving final adapter ...")
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)
    print(f"Done. Saved to {args.output_dir}")


if __name__ == "__main__":
    main()