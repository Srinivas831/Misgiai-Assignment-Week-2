import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments
from datasets import Dataset
from trl import RewardTrainer, RewardConfig
import torch
import matplotlib.pyplot as plt

# ==================================================
# ✅ STEP 1: Load the data
# ==================================================
data = pd.read_csv("data/prompt_answer_ranks.csv")

# ==================================================
# ✅ STEP 2: Convert ranks (1 -> best) to scores (5 -> best, 1 -> worst)
# ==================================================
data["score"] = 5 - data["rank"]

# ==================================================
# ✅ STEP 3: Create Hugging Face Dataset
# ==================================================
dataset = Dataset.from_pandas(data[["prompt", "answer", "score"]])

# ==================================================
# ✅ STEP 4: Load the base model and tokenizer
# ==================================================
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# IMPORTANT: GPT-style models don't have a padding token by default
tokenizer.pad_token = tokenizer.eos_token

# ==================================================
# ✅ STEP 5: Tokenization
# ==================================================
def tokenize(example):
    """Concatenate prompt and answer, then tokenize."""
    text = example["prompt"] + " " + example["answer"]
    return tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128,
    )

tokenized_ds = dataset.map(tokenize, batched=False)

# ==================================================
# ✅ STEP 6: Load Model
# ==================================================
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=1)

# ==================================================
# ✅ STEP 7: Training Args
# ==================================================
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    num_train_epochs=1,
    learning_rate=5e-5,
    save_strategy="no",
    logging_dir="./logs",
    logging_steps=10,
    remove_unused_columns=False,
)

# ==================================================
# ✅ STEP 8: Reward Model Configuration
# ==================================================
config = RewardConfig(
    output_dir="./results",
    per_device_train_batch_size=2,
    num_train_epochs=1,
    learning_rate=5e-5,
    bf16=False,
    fp16=False,
)


# ==================================================
# ✅ STEP 9: Initialize Reward Trainer
# ==================================================
train_ds = tokenized_ds  # ✅ DIRECTLY USE THE TOKENIZED DATASET
trainer = RewardTrainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    tokenizer=tokenizer,
)

# ==================================================
# ✅ STEP 10: Train the Model
# ==================================================
print("\n🚀 Starting Reward Model Training...")
train_results = trainer.train()
print("\n✅ Training Complete.")

# ==================================================
# ✅ STEP 11: Save Model
# ==================================================
model_dir = "./results"
model.save_pretrained(model_dir)
tokenizer.save_pretrained(model_dir)

# ==================================================
# ✅ STEP 12: Evaluate Model
# ==================================================
test_samples = [
    ("Why is the sky blue?", "Because it reflects the ocean."),
    ("Why is the sky blue?", "Due to Rayleigh scattering of light."),
    ("Why is the sky blue?", "I don’t know, maybe it's magic."),
]

# Load trained model
model = AutoModelForSequenceClassification.from_pretrained(model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_dir)

# Get reward scores
scores = []
for prompt, answer in test_samples:
    inputs = tokenizer(prompt + " " + answer, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        output = model(**inputs).logits
    scores.append(output.item())

# Print results
for (prompt, answer), score in zip(test_samples, scores):
    print(f"Prompt: {prompt}")
    print(f"Answer: {answer}")
    print(f"Reward Score: {score:.4f}\n")

# ==================================================
# ✅ STEP 13: Plot Results
# ==================================================
plt.figure(figsize=(8,5))
plt.bar(range(len(scores)), scores, tick_label=[f"Ans {i+1}" for i in range(len(scores))])
plt.ylabel("Reward Score")
plt.title("Reward Model Evaluation Results")
plt.show()
