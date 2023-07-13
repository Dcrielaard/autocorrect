" This file is the main file for an autocorrect function"

from autocorrect.vocabulair.ingestion import Vocabulair
from autocorrect.manipulations.manipulations import (
    delete_letter,
    insert_letter,
    replace_letter,
    switch_letter,
    edit_one_letter,
    edit_two_letters,
)


# Create the vocabulair of words
raw_vocab = Vocabulair.read_text_file("./data/shakespeare.txt")

print(f"The first ten words in the text are: \n{raw_vocab.text[0:10]}")
print(f"There are {len(raw_vocab.set_of_words)} unique words in the vocabulary.")
print(f"P('thee') is {raw_vocab.word_probabilities['thee']:.4f}")
print(f"There are {len(raw_vocab.word_counts)} key values pairs")
print(f"The count for the word 'thee' is {raw_vocab.word_counts.get('thee',0)}")

print(delete_letter(word="cans", verbose=True))
print(switch_letter(word="eta", verbose=True))
print(replace_letter(word="can", verbose=True))
print(insert_letter("at", True))


tmp_word = "at"
tmp_edit_one_set = edit_one_letter(tmp_word)
# turn this into a list to sort it, in order to view it
tmp_edit_one_l = sorted(list(tmp_edit_one_set))

print(f"input word {tmp_word} \nedit_one_l \n{tmp_edit_one_l}\n")
print(f"The type of the returned object should be a set {type(tmp_edit_one_set)}")
print(f"Number of outputs from edit_one_letter('at') is {len(edit_one_letter('at'))}")


tmp_edit_two_set = edit_two_letters("a")
tmp_edit_two_l = sorted(list(tmp_edit_two_set))
print(f"Number of strings with edit distance of two: {len(tmp_edit_two_l)}")
print(f"First 10 strings {tmp_edit_two_l[:10]}")
print(f"Last 10 strings {tmp_edit_two_l[-10:]}")
print(f"The data type of the returned object should be a set {type(tmp_edit_two_set)}")
print(
    f"Number of strings that are 2 edit distances from 'at' is {len(edit_two_letters('at'))}"
)
