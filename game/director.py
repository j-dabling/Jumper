from game.jumperman import jumper
from game.wordSelection.randomWord import randomWord

# Initializes all modules required for a game of jumper.
class director:
    def __init__(self):
        self.structure = jumper()
        self.word = randomWord()

    # Outputs the guessing_word and the jumper graphic to the terminal.
    def display(self):
        print(' '.join(self.word.guessing_word))
        for line in self.structure.parachute:
            print(line)
        for line in self.structure.man:
            print(line)

    # Starts and runs the game, checks for win conditions, and accepts user input.
    def start(self):
        # The loop will check to see if the word has been guessed completely,
        # or if the player has run out of guesses.
        while '_' in self.word.guessing_word and len(self.structure.parachute) > 0:
            self.display()
            
            guess = input('Guess a letter (a-z): ')
            if not self.word.isCorrect(guess):
                self.structure.cutLine()

        # Display the output one more time, then congratulate or console the player.
        self.display()
        if '_' not in self.word.guessing_word:
            print(f'Congradulations! You correctly guessed the word: "{self.word.guessing_word.capitalize()}"!')
        else:
            print("Whoops! You didn't guess the entire word in time!")