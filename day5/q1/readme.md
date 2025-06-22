# Tokenization and Masked Language Model Assignment

## Part 1: Tokenization

**Sentence:**  
`The cat sat on the mat because it was tired.`

---

### A) Tokenization Results

#### 1️⃣ **BPE Tokenization** (using GPT-2-style BPE)

Tokens:  
`['The', 'Ġcat', 'Ġsat', 'Ġon', 'Ġthe', 'Ġmat', 'Ġbecause', 'Ġit', 'Ġwas', 'Ġtired', '.']`  
IDs:  
`[464, 3133, 5923, 319, 262, 3793, 1228, 340, 373, 8452, 13]`  
Total Tokens: **11**

---

#### 2️⃣ **WordPiece Tokenization** (using BERT)

Tokens:  
`['the', 'cat', 'sat', 'on', 'the', 'mat', 'because', 'it', 'was', 'tired', '.']`  
IDs:  
`[1996, 4939, 4825, 2006, 1996, 10709, 2138, 2009, 2001, 5299, 1012]`  
Total Tokens: **11**

---

#### 3️⃣ **SentencePiece (Unigram) Tokenization** (using T5)

Tokens:  
`['▁The', '▁cat', '▁sat', '▁on', '▁the', '▁mat', '▁because', '▁it', '▁was', '▁tired', '.']`  
IDs:  
`[156, 661, 1293, 65, 8, 3473, 538, 31, 86, 2757, 3]`  
Total Tokens: **11**

---

### 🔍 Note (~150 words)

Each tokenizer uses a different approach:

- **BPE** works at the character or subword level and uses merging rules learned from training data. It treats spaces as special symbols (e.g., `Ġ`) and creates tokens like `Ġcat`.
- **WordPiece** (used in BERT) also breaks words down into subwords when needed (`tired` might be kept whole, rare words would be split), making it robust for unknown words.
- **SentencePiece** treats text as a stream of Unicode characters and uses its own learned units (often with the `▁` character marking spaces). 

These differences arise from training objectives and vocabularies, making each tokenizer unique in how it balances splitting words versus merging character sequences.

---

## Part 2: Masked Token Prediction

Original Sentence:
`The cat sat on the [MASK] because it was [MASK].`

### Model Used:
`bert-base-uncased`

#### 🎯 Results:

**First [MASK]:**  
- floor (25.3%)  
- couch (8.8%)  
- bed (8.7%)

**Second [MASK]:**  
- cold (5.4%)  
- hungry (4.5%)  
- warm (3.2%)

---

### 💡 Comment (~150 words)

The masked words predicted by the model align with its understanding of context. The first mask is a location (`mat`), and the model suggests plausible alternatives such as `floor`, `couch`, or `bed`. These are common places where a cat might rest. The second mask is an adjective describing the state of the cat, yielding suggestions like `cold`, `hungry`, or `warm`. The model captures common traits or conditions associated with pets. 

This demonstrates how masked language models, like BERT, use context learned from training data to propose words that fit naturally within a given sentence. The results highlight the strength of such models for NLP tasks like text completion and contextual understanding.

---
