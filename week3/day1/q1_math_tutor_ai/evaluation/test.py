import json
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))


# Import your prompt loader methods
from src.main import load_zero_shot_prompt, load_few_shot_prompt, load_cot_prompt, load_self_ask_prompt

# Load model and tokenizer
model_name = "Qwen/Qwen2.5-0.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Paths
test_file = os.path.join(os.path.dirname(__file__), "test_queries.jsonl")

# Prompt styles
PROMPT_FUNCTIONS = {
    "zero_shot": load_zero_shot_prompt,
    "few_shot": load_few_shot_prompt,
    "cot": load_cot_prompt,
    "self_ask": load_self_ask_prompt,
}

# Helper to run inference
def run_inference(prompt_func, user_question, max_new_tokens=100):
    prompt = prompt_func(user_question)
    encoding = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        output_ids = model.generate(
            encoding["input_ids"],
            attention_mask=encoding.get("attention_mask", None),
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Main testing loop
results = []
with open(test_file, "r") as f:
    for line in f:
        entry = json.loads(line.strip())
        user_question = entry["user_question"]

        result = {"user_question": user_question}
        for style_name, func in PROMPT_FUNCTIONS.items():
            result[style_name] = run_inference(func, user_question)

        results.append(result)

# Save results
out_file = os.path.join(os.path.dirname(__file__), "test_results.json")
with open(out_file, "w") as f:
    json.dump(results, f, indent=2)

print(f"Results saved to: {out_file}")

