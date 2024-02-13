import random


def validate_user_input(correct_letters, incorrect_letters):
    '''
    TODO: Implement the function according to the instructions
          provided in the document.

          1. Prompt the user for a letter.

          2. If the user input is a number, a special character or longer than
             a single charcter let them know why their input is invalid, and
             reprompt for the letter.

         3. If the letter is valid, return it.
    '''
    guess = input('\nEnter a letter: ').lower()

    return guess


def choose_word():
    '''
    TODO: Modify the implementation of this function according to the
          instructions provided in the document.

          1. Create an empty list called `titles`.

          2. Read the contents of the `titles.txt` file and store it inside the
             `titles` variable.

          3. Return a random element from the `titles` list.
    '''

    return 'Horrible Bosses'


def display_word(movie, correct_letters):
    '''
    This function prints the movie display. If a letter is present in the list
    of guessed_letters, it prints the letter; otherwise, it prints a dash.

    NOTE: Do not modify this function.
    '''
    # Iterate over each character in the movie title
    for c in movie:
        # If the character is a space, print a space; otherwise,
        # if it's a correct letter, print it; otherwise, print a dash.
        if c.isspace():
            print(' ', end=' ')
        elif c.lower() in correct_letters:
            print(c, end=' ')
        else:
            print('_', end=' ')
    # Print a new line
    print()


def check_win(movie_to_guess, correct_letters):
    '''
    This function returns True if each letter in movie appears in
    guessed_letters; otherwise, it returns False.

    NOTE: Do not modify this function.
    '''
    for c in movie_to_guess:
        if c != ' ' and c.lower() not in correct_letters:
            return False
    return True


def hm():
    # NOTE: You shouldn't have to change anything below here.

    # Initialize variables for the game
    movie_to_guess = choose_word()
    correct_letters = []
    incorrect_letters = []
    chances = 6

    # Greet the user and display the initial state of the game
    print("\nWelcome to Black History Month Hangman! \nCan you guess the film or show I have in mind?\n")
    display_word(movie_to_guess, correct_letters)

    # Play the game until the user wins or loses
    while True:

        # Validate user input for guessing a letter
        letter = validate_user_input(correct_letters, incorrect_letters)

        # Check if the guessed letter is correct or incorrect
        if letter in movie_to_guess.lower():
            correct_letters.append(letter)
            print('Good!\n')
        else:
            incorrect_letters.append(letter)
            chances -= 1
            print('Nope :(\n')

        # Display game progress to the user
        display_word(movie_to_guess, correct_letters)
        print(f'Correct letters: {correct_letters}')
        print(f'Incorrect letters: {incorrect_letters}')
        print(f'Chances: {chances}/6')

        # Check if the user has lost
        if chances < 1:
            print('\nYou lose. Try again.')
            break

        # Check if the user has won
        if check_win(movie_to_guess, correct_letters):
            print(f'\nYou did it! It was \'{movie_to_guess}\'. You\'re awesome.')
            break

    # Thank the user for playing the game
    print("\nThanks for playing Black History Month Hangman!\n")


if __name__ == "__main__":
    # Play the game.
    hm()
