"""
This files contains the various string manipulations
"""


class Manipulations:
    """
    This class hosts the different string manipulations
    which are a possible with single word.

    Args:
        word: string word where the string manipulations need to be applied on.

    """

    def __init__(self, word: str):
        self.word = word
        self.list_of_tuple_splits = self._split_word()

    def _split_word(self) -> list[tuple[str, str]]:
        splits_list = []
        for i in range(len(self.word)):
            splits_list.append((self.word[:i], self.word[i:]))
        return splits_list

    def delete_letter(self) -> list[str]:
        """
        This method will generate a list of all possible words which are possible by removing
        a single letter from a word

        Returns:
            delete_list: A list of all strings by deleting a single character from a word

        """
        delete_list = []
        for i in range(len(self.word)):
            delete_list.append(self.word[:i] + self.word[i + 1 :])
        return delete_list

    def switch_letter(self) -> list[str]:
        """
        This method generates a list of possible words by switching a single letter from a word.

        Returns:
            switch_list: A list of all strings where a single letter has been switched.

        """
        switch_list = []
        for _ in range(len(self.word)):
            switch_list = [
                L[:-1] + R[0] + L[-1] + R[1:]
                for L, R in self.list_of_tuple_splits
                if len(L) > 0
            ]

        return switch_list

    def replace_letter(self) -> list[str]:
        """
        This method returns a set of words where 1 letter has been switched with another letter

        Returns:
            replace_l: Set of words with 1 letter switched with another

        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        replace_l = []

        for _ in range(len(self.word)):
            replace_l = [
                a + l + (b[1:] if len(b) > 1 else "")
                for a, b in self.list_of_tuple_splits
                if b
                for l in letters
            ]

        replace_set = set(replace_l)
        replace_set.discard(self.word)
        return list(replace_set)

    def insert_letter(self) -> list[str]:
        """
        Method creates a list of words with an added single character

        Returns:
            insert_l: List of words where 1 character has been added.

        """

        letters = "abcdefghijklmnopqrstuvwxyz"
        insert_l = []
        split_l = []

        for i in range(len(self.word) + 1):
            split_l.append((self.word[:i], self.word[i:]))
            for character in letters:
                insert_l.append(self.word[:i] + character + self.word[i:])

        return insert_l


def edit_one_letter(word: str, allow_switches: bool = True) -> set[str]:
    """
    Input:
        word: the string/word for which we will generate all possible words that are one edit away.
    Output:
        edit_one_set: a set of words with one possible edit. Please return a set. and not a list.
    """

    edit_one_set: set[str] = set()

    manipulations = Manipulations(word)

    if allow_switches:
        list_of_words = (
            manipulations.insert_letter()
            + manipulations.replace_letter()
            + manipulations.switch_letter()
            + manipulations.delete_letter()
        )
    else:
        list_of_words = (
            manipulations.insert_letter()
            + manipulations.replace_letter()
            + manipulations.delete_letter()
        )

    edit_one_set = set(list_of_words)

    return set(edit_one_set)


def edit_two_letters(word: str, allow_switches: bool = True) -> set[str]:
    """
    Input:
        word: the input string/word
    Output:
        edit_two_set: a set of strings with all possible two edits
    """

    edit_two_set: set[str] = set()

    ones = edit_one_letter(word, allow_switches)

    for single_word in ones:
        edit_two_set = edit_two_set.union(edit_one_letter(single_word, allow_switches))

    return set(edit_two_set)
