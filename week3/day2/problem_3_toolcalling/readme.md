# 🧠 Tool-Enhanced Reasoning Script

This project demonstrates a Python-based reasoning assistant that accepts natural language queries, uses Chain-of-Thought (CoT) prompting with OpenAI's GPT, and calls real tool functions (like math or string utilities) when needed to compute accurate answers.

---

## 🚀 Features

- Takes a query from the user via command-line
- Uses OpenAI API (like GPT-3.5 or GPT-4) to:
  - Interpret the question step-by-step (CoT reasoning)
  - Determine whether a tool is needed
  - Specify the tool function to use (like `math.sqrt` or `string.count_vowels`)
- Calls actual Python functions for math/string operations
- Shows:
  - 🤔 LLM's step-by-step reasoning
  - 🛠️ Tool used (if any)
  - ✅ Final answer

---

## 🗂 Folder Structure

```
problem_3_toolcalling/
├── main.py
├── tools/
│   ├── math_tools.py
│   └── string_tools.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/problem_3_toolcalling.git
cd problem_3_toolcalling
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key:

Create a `.env` file:

```env
OPENAI_API_KEY=sk-your-key-here
```

---

## ▶️ Usage

Run the tool:

```bash
python main.py
```

Enter natural language queries like:

- `What's the square root of the average of 18 and 50?`
- `How many vowels are in the word 'Multimodality'?`
- `Is the number of letters in 'machine' greater than the vowels in 'reasoning'?`

---

## 🔧 Supported Tools

| Tool Function             | Description                             |
|--------------------------|-----------------------------------------|
| `math.sqrt(x)`           | Returns square root of `x`              |
| `math.average(a, b)`     | Returns average of `a` and `b`          |
| `string.count_vowels(s)` | Counts vowels (a, e, i, o, u) in string |
| `string.count_letters(s)`| Counts alphabetic letters in string     |

---

## 🧪 Sample Output

```bash
🔍 Enter your question: Is the number of letters in 'machine' greater than vowels in 'reasoning'?

🤔 Reasoning:
Step 1: Count letters in 'machine' = 7
Step 2: Count vowels in 'reasoning' = 4
Step 3: Compare 7 > 4 → True

🛠️ Tool Used: string.count_letters, string.count_vowels

✅ Final Answer: Yes, the number of letters in 'machine' is greater than the number of vowels in 'reasoning'.
```

---

## 🧠 Learning Concepts

- Chain-of-Thought (CoT) prompting
- Tool-calling using string detection and logic
- OpenAI API integration (chat completion)
- Python CLI + RegEx + modular function usage

---


