" This files contains the various string manipulations "


def delete_letter(word, verbose=False):
    """
    Input:
        word: the string/word for which you will generate all possible words
                in the vocabulary which have 1 missing character
    Output:
        delete_l: a list of all possible strings obtained by deleting 1 character from word
    """

    delete_l = []
    split_l = []

    for i in range(len(word)):
        split_l.append((word[:i], word[i:]))
        delete_l.append(word[:i] + word[i + 1 :])

    if verbose:
        print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")

    return delete_l


def switch_letter(word, verbose=False):
    """
    Input:
        word: input string
     Output:
        switches: a list of all possible strings with one adjacent charater switched
    """

    switch_l = []
    split_l = []

    for i in range(len(word)):
        split_l.append((word[:i], word[i:]))
        switch_l = [L[:-1] + R[0] + L[-1] + R[1:] for L, R in split_l if len(L) > 0]

    if verbose:
        print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}")

    return switch_l


def replace_letter(word, verbose=False):
    """
    Input:
        word: the input string/word
    Output:
        replaces: a list of all possible strings where we replaced one letter from the original word.
    """

    letters = "abcdefghijklmnopqrstuvwxyz"

    replace_l = []
    split_l = []

    for c in range(len(word)):
        split_l.append((word[0:c], word[c:]))
    replace_l = [
        a + l + (b[1:] if len(b) > 1 else "") for a, b in split_l if b for l in letters
    ]
    replace_set = set(replace_l)
    replace_set.discard(word)

    # turn the set back into a list and sort it, for easier viewing
    replace_l = sorted(list(replace_set))

    if verbose:
        print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")

    return replace_l


def insert_letter(word, verbose=False):
    """
    Input:
        word: the input string/word
    Output:
        inserts: a set of all possible strings with one new letter inserted at every offset
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    insert_l = []
    split_l = []

    for i in range(len(word) + 1):
        split_l.append((word[:i], word[i:]))

        for character in letters:
            insert_l.append(word[:i] + character + word[i:])

    if verbose:
        print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")

    return insert_l


def edit_one_letter(word, allow_switches=True):
    """
    Input:
        word: the string/word for which we will generate all possible words that are one edit away.
    Output:
        edit_one_set: a set of words with one possible edit. Please return a set. and not a list.
    """

    edit_one_set = set()

    ### START CODE HERE ###
    if allow_switches:
        list_of_words = (
            insert_letter(word)
            + replace_letter(word)
            + switch_letter(word)
            + delete_letter(word)
        )
    else:
        list_of_words = insert_letter(word) + replace_letter(word) + delete_letter(word)

    edit_one_set = set(list_of_words)

    ### END CODE HERE ###

    # return this as a set and not a list
    return set(edit_one_set)


def edit_two_letters(word, allow_switches=True):
    """
    Input:
        word: the input string/word
    Output:
        edit_two_set: a set of strings with all possible two edits
    """

    edit_two_set = set()

    ### START CODE HERE ###

    ones = edit_one_letter(word, allow_switches)
    for word in ones:
        edit_two_set = edit_two_set.union(edit_one_letter(word, allow_switches))

    ### END CODE HERE ###

    # return this as a set instead of a list
    return set(edit_two_set)
