import random


def get_rounds():
    """
    Allows the user to choose a number of rounds from 1 to 9.
    Returns the chosen number of rounds.
    """
    # TODO: Impelment the function as described.

def get_user_choice():
    """
    Presents the player with options and uses input() to get the player's move.
    Returns 'Rock', 'Paper', or 'Scissors'.
    """
    # TODO: Impelment the function as described.


def get_computer_choice():
    """
    Randomly generates the computer's move.
    Returns 'Rock', 'Paper', or 'Scissors'.

    Read the random documentation for choice here:
    https://www.w3schools.com/python/ref_random_choice.asp
    """
    options = ["Rock", "Paper", "Scissors"]

    # TODO: Use the choice function to return random computer choice.
    return None


def determine_winner(user_choice, computer_choice):
    """
    Determines the winner or if it's a tie based on the player and
    computer's move. Returns 'player', 'comp', or 'tie'.
    """
    # TODO: Impelment the function as described.


def rps():
    print("Welcome to Rock Paper Scissors!")
    rounds = get_rounds()
    print('-----------------')

    # TODO: Create three variables to track wins, losses and ties.

    for round in range(1, rounds + 1):
        print(f'Round: {round}')
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # TODO: Implement the game loop logic here.

        print('-----------------')

    # TODO: Display winner of the match.


if __name__ == "__main__":
    rps()
