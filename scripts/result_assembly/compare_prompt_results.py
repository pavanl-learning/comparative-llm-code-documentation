import json
from pathlib import Path

p1 = Path("outputs/evaluations/qwen25_1_5b_instruct_P1_zero_shot_summary.json")
p2 = Path("outputs/evaluations/qwen25_1_5b_instruct_P2_structured_summary.json")

with p1.open("r", encoding="utf-8") as f:
    a = json.load(f)

with p2.open("r", encoding="utf-8") as f:
    b = json.load(f)

keys = [
    "num_samples",
    "mean_latency_seconds",
    "mean_generated_word_count",
    "mean_rouge1_fmeasure",
    "mean_rouge2_fmeasure",
    "mean_rougeL_fmeasure",
    "mean_bertscore_f1",
]

print("P1_zero_shot vs P2_structured\n")
for k in keys:
    print(f"{k}")
    print(f"  P1: {a.get(k)}")
    print(f"  P2: {b.get(k)}")
    print()
