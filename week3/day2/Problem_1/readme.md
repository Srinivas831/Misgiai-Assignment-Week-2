# 🤖 Generative AI Model Comparison CLI Tool

This is a command-line tool to compare responses from different types of OpenAI models:
- **Base model** (`davinci-002`)
- **Instruct model** (`gpt-3.5-turbo`)
- **Fine-tuned model** (`ft:gpt-3.5-turbo:...` — optional)

The tool helps users understand how base, instruct-tuned, and fine-tuned models behave differently across various prompts.

---

## 🧪 Features

- Interactive CLI: Enter your model type and prompt.
- Calls OpenAI's latest API using the official `openai` Python SDK.
- Prints model metadata (name, description, context size).
- Helps collect data for analysis in `comparisons.md`.

---

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone
cd model-comparison-cli
