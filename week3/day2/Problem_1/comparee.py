import os
from dotenv import load_dotenv
from openai import OpenAI
import sys

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ Please set your OPENAI_API_KEY in the .env file.")
    sys.exit(1)

# ✅ Initialize OpenAI client
client = OpenAI(api_key=api_key)

# ✅ Model info
MODEL_INFO = {
    "base": {
        "name": "davinci-002",
        "description": "Base Model: A raw GPT-3-style LM that predicts text, not instruction-tuned.",
        "context": 4096
    },
    "instruct": {
        "name": "gpt-3.5-turbo",
        "description": "Instruct Model: GPT-3.5 tuned for chat and following instructions.",
        "context": 4096
    },
    "finetuned": {
        "name": "ft:gpt-3.5-turbo:your-fine-tuned-model-name",
        "description": "Fine-tuned Model: A GPT-3.5-turbo variant trained for a specific use case.",
        "context": 4096
    }
}

# ✅ Call model
def call_model(model_name, prompt):
    if model_name == "davinci-002":
        response = client.completions.create(
            model=model_name,
            prompt=prompt,
            max_tokens=256,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    else:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=256,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

# ✅ Main function
def main():
    print("🔍 Available model types: base, instruct, finetuned")

    model_type = input("➡️ Enter model type: ").strip().lower()
    if model_type not in MODEL_INFO:
        print("❌ Invalid model type. Please choose from: base, instruct, finetuned.")
        return

    prompt = input("📝 Enter your query: ").strip()
    spec = MODEL_INFO[model_type]
    result = call_model(spec["name"], prompt)

    print("\n✅ Model:", spec["name"])
    print("💡 Description:", spec["description"])
    print(f"📋 Context Window: ~{spec['context']} tokens\n")
    print("🗨️ Response:\n", result)

if __name__ == "__main__":
    main()
