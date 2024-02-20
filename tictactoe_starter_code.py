import random

PLAYER = 'player'
COMPUTER = 'computer'

def make_board():
    '''
    TODO: In this game, the board will be represented by a 3 x 3 matrix. This
          function should return a list of lists to represent the game board.

          Initially, each element in the list should be represented as an empty
          string. These empty strings will represent an empty space on the board.

    NOTE: Simply create a 3 x 3 matrix and return that variable.
    '''
    pass


def print_board(board):
    '''
    TODO: This function should print the game board for the user to view. The
          specific design of the board is up to you. If you don't have a preference,
          you can use the design provided in the example.

    NOTE: Instead of using a for loop, you can use print statements and the format function.
          https://www.w3schools.com/python/ref_string_format.asp
    '''
    pass


def get_player_move(board, player_team):
    '''
    TODO: This function should ask the user to input a row and column number to
          place their marker.

          If the chosen position is not empty (not a space) the function should
          repeatedly prompt the user for valid row and column numbers until a
          valid empty position is entered.

    NOTE: You can assume that a user of the game will always enter a number, but
          not neccessarily in the correct range [0, 2]. The could enter any integer.
    '''
    pass


def get_computer_move(board, computer_team):
    '''
    TODO: This function should return a marker ('X' or 'O') to an unoccupied
          position on the board.

    NOTE: This function might require some randomness.
    '''
    pass



def check_for_winner(board):
    '''
    TODO: This function should return one of the following: 'keep playing',
          'tie', or 'end game'.

          During each round, the program will assess whether the game should
          continue, end with a tie, or if there's a winner.

          If a marker ('X' or 'O') occupies all spaces vertically, horizontally,
          or diagonally, the function should return 'end game'.

          If all spaces are occupied but there's no winner, the function
          should return 'tie'.

          Otherwise, the function simply returns 'keep playing'.

    NOTE: For loops will be useful here.
    '''
    pass

# Now that we've defined our functions, let's play a game of tic-tac-toe!


# (Note: This `if` statement is important, please don't remove it.)
if __name__ == '__main__':
    print('\nWelcome to Tic-Tac-Toe!')

    # Ask the player what team they want to be.
    player_team = input('\nDo you want to be X or O? ').upper()

    if player_team == 'X':
        computer_team = 'O'
    else:
        computer_team = 'X'

    # Decide who goes first.
    whose_turn = random.choice([PLAYER, COMPUTER])
    print('\nThe {} will go first.'.format(whose_turn))

    # Get a fresh board.
    board = make_board()

    while True:
        # Figure out whose turn it is, and let them make a move.
        if whose_turn == PLAYER:
            print()
            print_board(board)
            print()
            get_player_move(board, player_team)
        else:
            get_computer_move(board, computer_team)

        # Check to see if someone won, and end the game if so.
        win_status = check_for_winner(board)
        if win_status != 'keep playing':
            if win_status == 'tie':
                print('\n-------------------')
                print("It's a tie!\n")
                print_board(board)
                print()
                break
            else:
                print('\n-------------------')
                print('The {} wins!\n'.format(whose_turn))
                print_board(board)
                print()
                break

        # If we've made it this far, nobody's won yet, so let's get ready for the next turn.
        if whose_turn == PLAYER:
            whose_turn = COMPUTER
        else:
            whose_turn = PLAYER
