from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# 1️⃣ Model Name
model_name = "Qwen/Qwen2.5-0.5B-Instruct"

# 2️⃣ Load Model & Tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 3️⃣ Helper: Load Zero-shot Prompt
def load_zero_shot_prompt(user_question: str) -> str:
    """Loads the zero-shot prompt and replaces {user_question}."""
    prompt_file = os.path.join(os.path.dirname(__file__), "../prompts/zero_shot.txt")
    # print(f"Looking for prompt file at: {os.path.abspath(prompt_file)}")
    # print(f"Exists? {os.path.exists(prompt_file)}") 
    with open(prompt_file, "r") as file:
        prompt_template = file.read()
    return prompt_template.format(user_question=user_question)

def load_few_shot_prompt(user_question: str) -> str:
    """Loads the few-shot prompt and replaces {user_question}."""
    prompt_file = os.path.join(os.path.dirname(__file__), "../prompts/few_shot.txt")
    with open(prompt_file, "r") as file:
        prompt_template = file.read()
    return prompt_template.format(user_question=user_question)

def load_cot_prompt(user_question: str) -> str:
    """Loads the CoT prompt and replaces {user_question}."""
    prompt_file = os.path.join(os.path.dirname(__file__), "../prompts/cot_prompt.txt")
    with open(prompt_file, "r") as file:
        prompt_template = file.read()
    return prompt_template.format(user_question=user_question)


def load_self_ask_prompt(user_question: str) -> str:
    """Loads the Self-Ask prompt and replaces {user_question}."""
    prompt_file = os.path.join(os.path.dirname(__file__), "../prompts/self_ask.txt")
    with open(prompt_file, "r") as file:
        prompt_template = file.read()
    return prompt_template.format(user_question=user_question)

# 4️⃣ Main
if __name__ == "__main__":
    #  zero shot
    # user_question = "What is the Pythagorean Theorem?"
    # Load prompt
    # prompt = load_zero_shot_prompt(user_question)

    # few
    # user_question = "What is the area of a circle with a radius of 5?"
    # # Try Few-shot
    # prompt = load_few_shot_prompt(user_question)

    # Chain of Thought
    # user_question = "If a car travels 60 km/h for 3 hours, how far will it go?"
    # prompt = load_cot_prompt(user_question)

    # Self-Ask
    user_question = "If a car goes 60 km/h for 3 hours and rests for 1 hour, what is the average speed?"
    prompt = load_self_ask_prompt(user_question)

    # Tokenize
    encoding = tokenizer(prompt, return_tensors="pt")
    input_ids = encoding["input_ids"]

    # Inference
    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            attention_mask=encoding.get("attention_mask", None),
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
        )
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Print
    print("\n=== Model Output (Zero-Shot) ===\n", response)
