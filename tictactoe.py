#Simple Tic Tac Toe game
#Two player
#Board prints each time a player makes a move
#Game accepts input of player and places symbol to board
import random

#global variable
the_board = [' ']*10

#set up board
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])

display_board(the_board)


#function to set player markers
def player_input():
    marker = ''
    #Ask player to select marker
    while marker != 'X' and marker!= 'O':
        marker = input('Player 1, choose X or O: ')
    #Assign opposite marker to Player 2
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

player_input()

def place_marker(board, marker, position):
    board[position] = marker

#win cases
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

#choose a player to start
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#check board space availability & if board is full
def space_check(board, position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#player input
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose the position for your marker(1-9): "))
    return position

#replay function
def replay():
    return input('Play again(Yes or No)?: ').lower().startswith('y')


#logic for game to operate
print('TIC-TAC-TOE')

while True:
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' is up first.')
    play_game = input('Are you ready to begin(Yes or No)?: ')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('You won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('It is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 wins!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('It is a draw')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break












