from transformers import AutoTokenizer

sentence = "The cat sat on the mat because it was tired."


# ==========================================================
# 2️⃣ Tokenizers
# ----------------------------------------------------------
# ✅ BPE Tokenizer: GPT-2 uses a BPE-style tokenizer
# ✅ WordPiece Tokenizer: BERT uses WordPiece
# ✅ SentencePiece Tokenizer: T5 uses SentencePiece (Unigram)
# ==========================================================

bpe_tokenizer = AutoTokenizer.from_pretrained("gpt2")
wordpiece_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
sentencepiece_tokenizer = AutoTokenizer.from_pretrained("t5-base")

bpe_tokens = bpe_tokenizer.tokenize(sentence)
bpe_ids = bpe_tokenizer.encode(sentence, add_special_tokens=False)

wordpiece_tokens = wordpiece_tokenizer.tokenize(sentence)
wordpiece_ids = wordpiece_tokenizer.encode(sentence, add_special_tokens=False)

sentencepiece_tokens = sentencepiece_tokenizer.tokenize(sentence)
sentencepiece_ids = sentencepiece_tokenizer.encode(sentence, add_special_tokens=False)


print("\n=== BPE Results (GPT-2) ===")
print("Tokens:",bpe_tokens)
print("Token ids:", bpe_ids)
print("Total Tokens", len(bpe_tokens))

print("\n=== WordPiece Results (BERT) ===")
print("Tokens:", wordpiece_tokens)
print("Token ids:", wordpiece_ids)
print("Total Tokens", len(wordpiece_tokens))

print("\n=== SentencePiece Results (T5) ===")
print("Tokens:", sentencepiece_tokens)
print("Token ids:", sentencepiece_ids)
print("Total Tokens", len(sentencepiece_tokens))



explanation = """
Each tokenization method segments text differently based on its training corpus and
encoding approach:
- BPE (Byte Pair Encoding): Merges frequent character sequences, yielding tokens
  like "tired" as a whole, making it efficient for common words.
- WordPiece: Similar to BPE but marks subwords with '##' when splitting rare words,
  making it suitable for diverse, multi-lingual text.
- SentencePiece (Unigram): Treats text as raw input, relying on a probabilistic
  model for splitting, yielding unique tokens for rare or complex words.

These differences arise because each approach optimizes for different goals:
dictionary efficiency, character coverage, and language variability.
"""
