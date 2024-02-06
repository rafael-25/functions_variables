import random

# TODO: Add at least 5 movie titles into the following list.
#       For example, ['Shrek', 'Taken', 'Baby Boy', etc...]
movie_titles = []

def choose_word(movie_titles):
    '''
    This function returns a random word from a list of movie titles.
    '''
    # TODO: Implement function as described above.
    pass

def display_word(movie_to_guess, guessed_letters):
    '''
    This function prints the movie display. If a letter is present in the list
    of guessed_letters, it prints the letter; otherwise, it prints a dash.

    For example, if the movie is 'Apollo' and the guessed letters are
    ['a', 'o'], the function would print: a _ o _ _ o

    Be mindful, what should be done if the movie title includes a
    space?
    '''
    # TODO: Implement function as described above.
    pass

def check_win(movie_to_guess, guessed_letters):
    '''
    This function returns True if each letter in movie appears in
    guessed_letters; otherwise, it returns False.

    For example, if the movie is 'Apollo' and guessed_letters is
    ['a','o','p','l'], the function would return True because each letter in the
    movie appears in the list; however, if guessed_letters were ['o', 'p', 'l'],
    it would return False because the letter 'a' is missing.

    Be mindful, spaces should not be considered.
    '''
    # TODO: Implement function as described above.
    pass

def hangman():
    movie_to_guess = choose_word(movie_titles)
    guessed_letters = []
    incorrect_letters = []
    chances = 6

    print("\nWelcome to Movie Hangman! Can you guess the film I have in mind?\n")
    print("The film is...")

    # TODO: Call the display_word function


    while True:

        # TODO: Ask the user for a letter, ensure it is always lowercase.


        # TODO: Use conditional statements to verify if the guess was correct or incorrect.
        #       Be sure to update variables as necessary.


        # TODO: Display the word, incorrect/correct letters, and chances.


        # TODO: If the player runs out of chances, break out the loop because the player loses.


        # TODO: If the player guesses the word correctly, break out the loop because the player wins.

if __name__ == "__main__":
    hangman()

print("\nThanks for playing Movie Hangman!\n")
