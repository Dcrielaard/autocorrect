" This file is used for the creation of a autocorrect vocabulair. "

import re

class Vocabulair:
    def __init__(self, text):
        self.text = text
        

    @classmethod
    def read_text_file(cls, file_name: str) -> list:
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
            list_of_words = re.findall(r'\w+', line)
            for word in list_of_words:
                words.append(word)
        
        return cls(words)
    

    def get_count(self) -> dict:
        """
        This method creates a dictionary of words and word counts from a corpus.

        Input:
            set_of_words: a set of words representing the corpus. 

        Output:
            word_count_dict: The wordcount dictionary where key is the word and value is its frequency.
        """
        
        word_count_dict = {}

        for word in self.text:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1
                

        return word_count_dict
    

    def get_word_probabilities(word_count_dict):
        """
        This method determines the probability that a words occurs in vector of words. 

        Input:
            word_count_dict: The wordcount dictionary where key is the word and value is its frequency.

        Output:
            probs: A dictionary where keys are the words and the values are the probability that a word will occur. 
        """
        probs = {}  # return this variable correctly
        

        for key, value in word_count_dict.items():
            probs[key] = value / sum(word_count_dict.values())
        
        # get the total count of words for all words in the dictionary
        
        return probs