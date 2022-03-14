from random import choice
from zipapp import create_archive


class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = SpecialWordFinder("words2.txt")
    4 words read

    >>> rand_word = wf.random()

    >>> rand_word in wf.word_list
    True
    """

    def __init__(self, location):
        self.word_list = list()
        self.create_word_list(self.open_file(location))
        return print(f"{len(self.word_list)} words read")

    def open_file(self, location):
        file = open(location, 'r')
        return file

    def create_word_list(self, file):
        for line in file:
            self.word_list.append(line.strip("\n"))
        file.close()

    def random(self):
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """find words in a file with comments denotateds by "#" as well as blank space lines"""

    def __init__(self, location):
        super().__init__(location)

    def create_word_list(self, file):
        for line in file:
            if line.startswith(" ") or line.startswith("#") or line.startswith("\n"):
                continue
            else:
                self.word_list.append(line.strip("\n"))
        file.close()
