"""
This file contains the different corrections.
"""

from autocorrect.manipulations import edit_one_letter, edit_two_letters


def get_corrections(word, probs, vocab, n=2, verbose = False):
    '''
    Input: 
        word: a user entered string to check for suggestions
        probs: a dictionary that maps each word to its probability in the corpus
        vocab: a set containing all the vocabulary
        n: number of possible word corrections you want returned in the dictionary
    Output: 
        n_best: a list of tuples with the most probable n corrected words and their probabilities.
    '''
    
    suggestions = []
    n_best = []
    
    if word in vocab:
        suggestions.append(word)
    
    if len(suggestions) == 0:
        one_letter_suggestions = edit_one_letter(word)
    
        for one_letter_suggestion in one_letter_suggestions:
            if one_letter_suggestion in vocab:
                suggestions.append(one_letter_suggestion)
                
    if len(suggestions) == 0:
        two_letter_suggestions = edit_two_letters(word)
    
        for two_letter_suggestion in two_letter_suggestions:
            if two_letter_suggestion in vocab:
                suggestions.append(two_letter_suggestion)
    
    if len(suggestions) == 0:
        suggestions.append(word)
            
            
    # Step 2: determine probability of suggestions
    for suggestion in suggestions:
        n_best.append((suggestion, probs.get(suggestion, 0)))
    
    #Step 3: Get all your best words and return the most probable top n_suggested words as n_best
    n_best = sorted(n_best, key=lambda tup: tup[1], reverse = True)
    n_best = n_best[0:5]
    
    
    if verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)

    return n_best