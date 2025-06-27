# tools/string_tools.py

# This function counts the number of vowels in a word
def count_vowels(word):
    return sum(1 for ch in word.lower() if ch in 'aeiou')

# This function counts all letters (length of the word)
def count_letters(word):
    return len(word)
