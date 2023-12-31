"""
This file is the main file for an autocorrect function
"""

from autocorrect.ingestion import Vocabulair
from autocorrect.corrections import get_corrections


# Create the vocabulair of words
raw_vocab = Vocabulair.read_text_file("./data/shakespeare.txt")

# print(f"The first ten words in the text are: \n{raw_vocab.text[0:10]}")
# print(f"There are {len(raw_vocab.set_of_words)} unique words in the vocabulary.")
# print(f"P('thee') is {raw_vocab.word_probabilities['thee']:.4f}")
# print(f"There are {len(raw_vocab.word_counts)} key values pairs")
# print(f"The count for the word 'thee' is {raw_vocab.word_counts.get('thee',0)}")


"""
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
"""

# manipulater = Manipulations("Dennis")
# print(manipulater.delete_letter())
# print(manipulater.switch_letter())
# print(manipulater.replace_letter())
# print(manipulater.insert_letter())
# print(len(edit_two_letters("dennis")))

vocab = raw_vocab.word_counts
probs = raw_vocab.word_probabilities


# Test your implementation - feel free to try other words in my word
my_word = "dys"


tmp_corrections = get_corrections(
    my_word, probs, vocab, 2, verbose=True
)  # keep verbose=True
for i, word_prob in enumerate(tmp_corrections):
    print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")
