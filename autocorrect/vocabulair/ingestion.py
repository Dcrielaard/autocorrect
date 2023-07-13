" This file is used for the creation of a autocorrect vocabulair. "

import re
from typing import Dict


class Vocabulair:
    """
    This class serves as the vocabulair for the autocorrect function.
    To generate the vocabulair, a list of words needs to be supplied.
    This can be done by passing a list of words to the class constructor,
    or by supplying the 'read_text_file' method the location to a file.

    """

    def __init__(self, text: list[str]):
        self.text = text
        self.set_of_words = self._set_of_words()
        self.word_counts = self.get_word_count()
        self.word_probabilities = self.get_word_probabilities()

    @classmethod
    def read_text_file(cls, file_name: str) -> "Vocabulair":
        """
        This method reads in a text file and returns a list of words in lower case.

        Input:
            A file_name which is found in your current directory. You just have to read it in.

        Output:
            words: a list containing all the words in the corpus (text file you read) in lower case.
        """
        words = []

        fhand = open(file_name)
        for line in fhand:
            line = line.lower()
            list_of_words = re.findall(r"\w+", line)
            for word in list_of_words:
                words.append(word)

        return cls(words)

    def _set_of_words(self) -> set[str]:
        """
        This method creates as set of words from the initial text.

        Output:
            set of words

        """
        return set(self.text)

    def get_word_count(self) -> Dict[str, int]:
        """
        This method creates a dictionary of words and word counts from a corpus.

        Input:
            set_of_words: a set of words representing the corpus.

        Output:
            word_count_dict: Dictionary where key is the word and value is its frequency.
        """

        word_count_dict: dict[str, int] = {}

        for word in self.text:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

        return word_count_dict

    def get_word_probabilities(self) -> dict[str, float]:
        """
        This method determines the probability that a words occurs in vector of words.

        Input:
            word_count_dict: Dictionary where key is the word and value is its frequency.

        Output:
            probs: Dictionary where keys are the words
              and the values are the probability that a word will occur.
        """
        probs = {}  # return this variable correctly

        for key, value in self.word_counts.items():
            probs[key] = value / sum(self.word_counts.values())

        # get the total count of words for all words in the dictionary

        return probs
