#Simple Tic Tac Toe game
#Two player
#Board prints each time a player makes a move
#Game accepts input of player and places symbol to board

#from IPython.display import clear_output

#set up board
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])

test_board = [' ']*10
display_board(test_board)


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