import json
from transformers import pipeline

# ---------------------------------------------------
# STEP 1: Load the KB
# ---------------------------------------------------
with open("kb.json", "r") as f:
    knowledge_base = json.load(f)

# ---------------------------------------------------
# STEP 2: All questions we'll test
# ---------------------------------------------------
test_questions = [
    # 10 questions from the KB
    *[entry["question"] for entry in knowledge_base],
    # 5 out-of-domain questions
    "What is the best programming language?",
    "How tall is the Empire State Building?",
    "What is the meaning of life?",
    "Where is the Eiffel Tower located?",
    "What is the fastest car in the world?"
]

# ---------------------------------------------------
# STEP 3: Initialize the Model
# ---------------------------------------------------
model_name = "google/flan-t5-base"  # Small, instruction-tuned
llm_pipeline = pipeline("text2text-generation", model=model_name)

# ---------------------------------------------------
# STEP 4: Loop through questions
# ---------------------------------------------------
for user_question in test_questions:
    print("\n--------------------------------------")
    print(f"Q: {user_question}")

    # Find match in KB
    matched_entry = None
    for entry in knowledge_base:
        if entry["question"].lower() == user_question.lower():
            matched_entry = entry
            break

    # ---------------------------------------------------
    # STEP 5: Get LLM's Answer
    # ---------------------------------------------------
    llm_answer = llm_pipeline(user_question, max_new_tokens=30)[0]["generated_text"].strip()
    print(f"LLM Answer: {llm_answer}")

    # ---------------------------------------------------
    # STEP 6: Validate
    # ---------------------------------------------------
    if matched_entry:
        if matched_entry["answer"].lower() == llm_answer.lower():
            print("\n✅ CORRECT: LLM's answer matches KB.")
        else:
            print("\n❌ RETRY: Answer differs from KB.")
    else:
        print("\n⚠️ RETRY: Out-of-domain question.")
