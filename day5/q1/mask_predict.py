# ==========================================================
# PART 2: MASK FILLING USING BERT
# ==========================================================
# Goal:
# - We have a sentence with [MASK] tokens.
# - We will load a BERT model and use it to fill the masks.
# - Then we'll display the top-3 suggestions and briefly
#   comment on their plausibility.
# ===========================================================

# STEP 1: Import the required Hugging Face transformers pipeline
from transformers import pipeline

# STEP 2: Create the fill-mask pipeline using the BERT model
# - "fill-mask" is a special pipeline for mask prediction.
# - "bert-base-uncased" is a popular model trained for masked LM.
mask_filler = pipeline("fill-mask", model="bert-base-uncased")

# STEP 3: Create your masked sentence.
# Here, we've replaced "mat" and "tired" with [MASK].
masked_sentence = "The cat sat on the [MASK] because it was [MASK]."

# STEP 4: Get the fill-mask results.
# IMPORTANT:
# The pipeline returns a list of results for EACH mask position.
results = mask_filler(masked_sentence, top_k=3)

# STEP 5: Interpret Results
# Hugging Face returns a list of lists:
# results[0] -> Suggestions for the first [MASK]
# results[1] -> Suggestions for the second [MASK]

# STEP 6: Print results
mask_positions = ["first [MASK]", "second [MASK]"]

for i, mask_results in enumerate(results):
    print(f"\nResults for {mask_positions[i]} position:\n")
    for result in mask_results:
        token = result["token_str"].strip()
        score = result["score"]
        print(f"  - Token: '{token}' (Confidence: {score:.4f})")

    # STEP 7: Add your short comment (you can customize!)
    if i == 0:
        print("\nComment: The first mask is expected to be something like 'mat', 'bed', or 'floor'. These fit well with a cat sitting on something.\n")
    else:
        print("\nComment: The second mask is expected to be an adjective related to the state of the cat. Words like 'tired', 'sleepy', or 'hungry' make sense.\n")

