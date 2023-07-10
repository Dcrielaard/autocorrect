" This file is the main file for an autocorrect function"

from autocorrect.vocabulair.word_propabilities import get_count, get_probs
from autocorrect.vocabulair.ingestion import Vocabulair

"""
# Create the vocabulair of words
raw_vocab = Vocabulair.read_text_file("./data/shakespeare.txt")
vocab = set(raw_vocab.text)


print(f"The first ten words in the text are: \n{raw_vocab.text[0:10]}")
print(f"There are {len(vocab)} unique words in the vocabulary.")

word_count_dict = raw_vocab.get_word_count()

print(f"There are {len(word_count_dict)} key values pairs")
print(f"The count for the word 'thee' is {word_count_dict.get('thee',0)}")

probs = get_probs(word_count_dict)
print(f"Length of probs is {len(probs)}")
print(f"P('thee') is {probs['thee']:.4f}")

"""

lijstje = ["a", "a", "v", "d"]

voc = Vocabulair(lijstje)
print(voc.word_probabilities["a"])
