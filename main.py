from director import director

# Initializes director class and starts the game.
def main():
    game = director()
    game.start()

    again = input('Would you like to play again? (y/n)')
    if again.lower() == 'y':
        main()
    else:
        print('Thank you for playing!')

main()