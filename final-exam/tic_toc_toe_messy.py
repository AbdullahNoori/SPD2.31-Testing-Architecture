import random

BOARD_SPACE = 10

def draw_board(board):
    """ This function prints out the board that it was passed.
    board is a list of 10 strings representing the board (ignore index 0)"""
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    """ Returns a list with the player’s letter as the first item, 
        and the computer's letter as the second."""
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

        #first element is player’s letter,second is computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:                       
            return ['O', 'X']

def first_player():
    """ Randomly choose the player who goes first."""
    if random.randint(0, 1) == 0:
        return 'computer'
    else:                       
        return 'player'

def play_again():
    """ Function returns True if player wants to play again, otherwise returns False."""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    """ Given a board and a player’s letter, this function returns True if that player has won.
        We use bo instead of board and le instead of letter so we don’t have to type as much."""
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle    # TODO: Fix the indentation of this lines and the following ones.
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def get_board_copy(board):
    """Duplicates the board list & returns it duplicate."""
    BoardCopy = []
    board_length = len(board)

    for i in range(board_length):
        BoardCopy.append(board[i])

    return BoardCopy

def is_space_free(board, move):
    """ Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def get_player_move(board):
    """ Let the player type in their move."""
    player_move = ' '
    while player_move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(player_move)):
        print('What is your next move? (1-9)')
        player_move = input()
    return int(player_move)

def choose_random_move_from_list(board, movesList):
    """ Returns valid move from passed list on the passed board.
        Returns None if there is no valid move."""
    possible_moves = []
    for move in movesList:
        if is_space_free(board, move):
            possible_moves.append(move)

    if len(possible_moves) != 0: # TODO: How would you write this pythanically? (You can google for it!)
        return random.choice(possible_moves)
    return None

def get_computer_move(board, computerLetter): # TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    """ Given a board and the computer's letter, determine where to move and return that move."""
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, len(board)):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computerLetter, i)
            if is_winner(copy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, playerLetter, i)
            if is_winner(copy, playerLetter):
                return i
    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None: # TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    """ Return True if every space on the board has been taken. Otherwise return False."""
    for i in range(1,BOARD_SPACE):
        if is_space_free(board, i):
            return False  
    return True

# TODO: The following mega code block is a huge hairy monster. Break it down 
# into smaller methods. Use TODO s and the comment above each section as a guide 
# for refactoring.
def run_game():
    """function to run game"""
    while True:
        """ Reset the board"""
        theBoard = [' '] * BOARD_SPACE # TODO: Refactor the magic BOARD_SPACE in this line (and all of the occurrences of 10 thare are conceptually the same.)
        playerLetter, computerLetter = input_player_letter()
        turn = first_player()
        print('The ' + turn + ' will go first.')
        game_is_on = True # TODO: Study how this variable is used. Does it ring a bell? (which refactoring method?) 
                            #       See whether you can get rid of this 'flag' variable. If so, remove it.

        while game_is_on: # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
                            #       Use a meaningful name for the function you choose.
            if turn == 'player':
                # Player’s turn.
                draw_board(theBoard)
                move = get_player_move(theBoard)
                make_move(theBoard, playerLetter, move)

                if is_winner(theBoard, playerLetter):
                    draw_board(theBoard)
                    print('Hooray! You have won the game!')
                    game_is_on = False
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break
                
                turn = 'computer'

            else:
                # Computer’s turn.
                move = get_computer_move(theBoard, computerLetter)
                make_move(theBoard, computerLetter, move)

                if is_winner(theBoard, computerLetter):
                    draw_board(theBoard)
                    print('The computer has beaten you! You lose.')
                    game_is_on = False
                if is_board_full(theBoard):
                    draw_board(theBoard)
                    print('The game is a tie!')
                    break

                turn = 'player'

        if not play_again():
            break

run_game()

