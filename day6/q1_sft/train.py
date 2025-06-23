from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model
import os
import json

# =========================================================
# PART 1: LOAD DATASET
# =========================================================
dataset = load_dataset("json", data_files="dataset.jsonl", split="train")
print("\n✅ Dataset Loaded:", dataset)

# =========================================================
# PART 2: LOAD MODEL & TOKENIZER
# =========================================================
model_name = "distilgpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# IMPORTANT: Set padding token
tokenizer.pad_token = tokenizer.eos_token
print("\n✅ Model and Tokenizer Loaded.")

# =========================================================
# PART 3: TOKENIZATION FUNCTION
# =========================================================
def tokenize(example):
    """Tokenizes a single example from the dataset and adds labels."""
    text = example["text"]

    tokenized = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128,
    )
    # IMPORTANT: Labels are the input ids for LM
    tokenized["labels"] = tokenized["input_ids"].copy()
    return tokenized


# Apply the tokenizer
tokenized_ds = dataset.map(tokenize)
# IMPORTANT: Remove original text column
tokenized_ds = tokenized_ds.remove_columns(["text"])

# =========================================================
# PART 4: TRAINING CONFIG
# =========================================================
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    learning_rate=5e-5,
    save_strategy="no",
    logging_dir="./logs",
    logging_steps=10,
    remove_unused_columns=False,
)

print("\n✅ TrainingArguments configured.")

# =========================================================
# PART 5: MODEL WRAPPING WITH LoRA + TRAINER
# =========================================================
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM",
)

model = get_peft_model(model, lora_config)

print("\n✅ Model wrapped with LoRA.")

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_ds,
    tokenizer=tokenizer
)

# =========================================================
# PART 6: START TRAINING
# =========================================================
print("\n🚀 Starting Training...")
train_results = trainer.train()
metrics = train_results.metrics
print("\n✅ Training Complete. Metrics:", metrics)

# Save training results
results_file = "./results/training_results.json"

with open(results_file, "w") as f:
    json.dump(train_results.metrics, f, indent=4)

# =========================================================
# PART 7: SAVE THE MODEL
# =========================================================
save_dir = "./fine_tuned_model"
os.makedirs(save_dir, exist_ok=True)

model.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)

print(f"\n✅ Model and Tokenizer saved to: {save_dir}")

# =========================================================
# PART 8: LOAD THE FINE-TUNED MODEL
# =========================================================
fine_tuned_model_dir = "./fine_tuned_model"

model = AutoModelForCausalLM.from_pretrained(fine_tuned_model_dir)
tokenizer = AutoTokenizer.from_pretrained(fine_tuned_model_dir)

tokenizer.pad_token = tokenizer.eos_token
print("\n✅ Fine-tuned Model Loaded.")

# =========================================================
# PART 9: TEST THE MODEL
# =========================================================
test_question = "What is the capital of France?"
input_ids = tokenizer.encode(test_question, return_tensors="pt")

# Get the model's output
output_ids = model.generate(input_ids, max_new_tokens=30, do_sample=True, temperature=0.7)

answer = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print("\nQuestion:", test_question)
print("Answer:", answer)
