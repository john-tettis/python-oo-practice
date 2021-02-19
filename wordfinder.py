
from random import choice

class WordFinder:
    """Collects words from text file and has methods to return random word"""
    

    def __init__(self, path):
        """Creates file, words variables and prints the number of words read in path"""
        self.file = open(path, 'r')
        self.words = self.read_file(self.file)
        print(f'{len(self.words)} words read')

    @classmethod
    def read_file(self, file):
        """Reads an open file line by line and adds each word  to a list and returns it"""
        words = []
        for line in file:
            words.append(line.removesuffix('\n'))
        return words

    def random(self):
        return choice(self.words)



class SpecialWordFinder(WordFinder):
    """Finds words and searches around comments(#) and blank lines"""
    def __init__(self, path):
        super().__init__(path)
    @classmethod
    def read_file(self, file):
        """parses through eaach line in the file including the word if the line does not start with #, and is not empty."""
        return [word.strip() for word in file if word.strip() and not word.startswith('#')]