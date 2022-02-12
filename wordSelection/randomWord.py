# The word class will choose a random word, then send the number of characters in the word to the director class.
# _complete_word The chosen word from the word list. Should be set to private.
# guessing_word The filled-in letters that the player has guessed of the word. Missing letters are represented by '_'.
# isCorrect(letter) Checks if letter is in complete_word. If it is then letter will be added into guessing_word and returns True.
#                   Otherwise returns False.
import random

class randomWord:
    _complete_word = ''
    guessing_word = ''

    def __init__(self):
        # words.txt contains a list of many words to choose from.
        # Credit for making the list goes to user dwyl on github:
        # https://github.com/dwyl/english-words
        wordList = open('wordSelection/words.txt', 'r')
        self._complete_word = random.choice(wordList.readlines())

        # # guessing_word must be the length of _complete_word.
        # Each space is set to an underscore to represent a blank space.
        self.guessing_word = '_' * len(self._complete_word)

    # Strings are immutable in python, so this will take the string apart, 
    # then return a new string with the replaced character included.
    def replaceChar(self, index, replacement):
        return '%s%s%s'%(self.guessing_word[:index],replacement,self.guessing_word[index+1:])
    

    # Given a letter (char) guess from the player, checks if their guess is correct.
    # Returns True if correct, False otherwise.
    def isCorrect(self, letter):
        if letter in self._complete_word:
            # Place the letter in the correct place in guessing word.
            for i in range(len(self._complete_word)):
                if self._complete_word[i] == letter:
                    #self.guessing_word[i] = letter
                    self.guessing_word = self.replaceChar(i, letter.upper())

            # Return true to show that the guess was correct.
            return True
        else:
            return False