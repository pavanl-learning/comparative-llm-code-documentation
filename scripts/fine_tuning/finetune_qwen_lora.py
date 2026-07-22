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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", required=True)
    parser.add_argument("--valid", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model-name", default="Qwen/Qwen2.5-Coder-1.5B-Instruct")
    parser.add_argument("--max-length", type=int, default=1024)
    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    train_ds = load_dataset("json", data_files=args.train)["train"]
    valid_ds = load_dataset("json", data_files=args.valid)["train"]

    train_ds = train_ds.map(
        lambda x: tokenize_fn(x, tokenizer, args.max_length),
        remove_columns=train_ds.column_names,
    )
    valid_ds = valid_ds.map(
        lambda x: tokenize_fn(x, tokenizer, args.max_length),
        remove_columns=valid_ds.column_names,
    )

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
    )
    model = prepare_model_for_kbit_training(model)

    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj"
        ],
    )
    model = get_peft_model(model, peft_config)

    training_args = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        gradient_accumulation_steps=8,
        learning_rate=2e-4,
        num_train_epochs=2,
        warmup_ratio=0.03,
        weight_decay=0.01,
        logging_steps=10,
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

    trainer.train()
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)


if __name__ == "__main__":
    main()