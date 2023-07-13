" This file is the main file for an autocorrect function"

from autocorrect.vocabulair.ingestion import Vocabulair


# Create the vocabulair of words
raw_vocab = Vocabulair.read_text_file("./data/shakespeare.txt")

print(f"The first ten words in the text are: \n{raw_vocab.text[0:10]}")
print(f"There are {len(raw_vocab.set_of_words)} unique words in the vocabulary.")
print(f"P('thee') is {raw_vocab.word_probabilities['thee']:.4f}")
print(f"There are {len(raw_vocab.word_counts)} key values pairs")
print(f"The count for the word 'thee' is {raw_vocab.word_counts.get('thee',0)}")
