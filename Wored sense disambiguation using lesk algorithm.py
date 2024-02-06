from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# The sentence you want to disambiguate
sentence = "The river bank is full of sand."

# The word you want to disambiguate
word = "bank"

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Use the Lesk algorithm to disambiguate the word
sense = lesk(tokens, word)

# Print the result
print("The word '{}' in the sentence '{}' most likely refers to the sense: {}".format(word, ' '.join(tokens), sense))
