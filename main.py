import os

class Scrabble:
    def __init__(self):
        self.scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
                     "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
                     "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
                     "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
                     "x": 8, "z": 10}
        current_directory = os.path.dirname(os.path.abspath(__file__))
        words_file = os.path.join(current_directory, "words.txt")
        self.word_list = set(open(words_file, "r").read().splitlines())
    
    def score_word(self, word):
        return sum(self.scores.get(char.lower(), 0) for char in word)

game = Scrabble()
word = input("Enter a word: ")
if word.lower() in game.word_list:
    print("Score for the word '{}': {}".format(word, game.score_word(word)))
else:
    print("\033[91mThe word '{}' is not in the dictionary.\033[0m".format(word))
