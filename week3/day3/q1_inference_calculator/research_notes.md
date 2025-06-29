# 📖 LLM Inference: Research Notes

## 🔍 What is Inference in LLMs?

Inference is the process of using a trained language model to generate output from a given input prompt. Unlike training or fine-tuning (where the model's weights are updated), inference simply runs the model **forward** to produce predictions.

Example:
- Input: "Translate to French: Hello"
- Output: "Bonjour"

The model processes input tokens and produces output tokens one-by-one using its internal weights.

---

## ⚙️ Key Factors That Affect Inference

### 1. **Model Size (e.g., 7B, 13B, GPT-4)**
- The number of parameters in the model (e.g., 7 billion) directly affects:
  - Memory consumption (RAM/VRAM)
  - Latency (slower for larger models)
  - Accuracy and capability (larger → better performance)

### 2. **Token Count**
- Input and output are broken down into tokens (e.g., "Translate to French" → 4 tokens).
- More tokens = more computation = more latency and memory usage.

### 3. **Batch Size**
- How many prompts are processed simultaneously.
- Higher batch size improves throughput but increases memory requirement.

### 4. **Hardware Type**
- GPU: Fastest, optimized for parallel token generation.
- CPU: Slower, but more widely available.
- TPU: Specialized, rare in public setups.

### 5. **Deployment Mode**
- **Cloud (API-based)**: e.g., OpenAI's GPT-4 — you pay per token.
- **Local (on-prem)**: e.g., running LLaMA 2 on your own GPU or server.
- **Edge**: Tiny models running on mobile/IoT — rare for LLMs.

---

## 📊 Model Comparison Table

| Feature               | 7B (e.g., LLaMA 2) | 13B (e.g., LLaMA 2) | GPT-4 (OpenAI)       |
|-----------------------|-------------------|---------------------|-----------------------|
| Parameters            | 7 Billion         | 13 Billion          | ~170 Billion (est.)   |
| VRAM Required         | ~16 GB            | ~26 GB              | ~45–80 GB (est.)      |
| Speed (tokens/sec)    | 50–100 (GPU)      | 30–60 (GPU)         | 10–30 (API-limited)   |
| Context Length        | 4k–32k            | 4k–32k              | 128k (GPT-4-turbo)    |
| Inference Latency     | ~100–300ms        | ~200–500ms          | ~1–2s                 |
| Cost                  | Free (local)      | Free (local)        | $0.01–$0.06 / 1K tokens |
| Use Case Suitability  | Lightweight apps  | Advanced use cases  | High-end prod use     |
# 🤖 LLM Inference Calculator

This project provides a command-line calculator that estimates inference latency, memory usage, and cost for different Large Language Models (LLMs), such as 7B, 13B, and GPT-4.

---

## 📦 Project Structure


---

## 🧠 Summary

- Inference is the forward pass of a trained LLM to get answers.
- The bigger the model and prompt, the more memory and latency.
- Cloud APIs like OpenAI provide simplicity but cost money.
- Local models are free to run but need powerful GPUs.




---

## 🧠 What is This?

LLM inference is the process of generating output from a trained model. This tool helps estimate:

- ⏱️ **Latency** – How long the model takes to return an output
- 💾 **Memory Usage** – How much VRAM or RAM is used during inference
- 💰 **Cost per request** – Approximate token-based pricing for hosted APIs

This is especially useful when comparing on-premise vs cloud deployment strategies for models of different sizes.

---

## 🔧 How to Run

### 1. Prerequisites

- Python 3.7+
- Terminal or command prompt access

### 2. Run the CLI Tool

```bash
python inference_calculator.py --model_size 7B --tokens 1000 --batch_size 2 --hardware_type GPU --deployment_mode local
