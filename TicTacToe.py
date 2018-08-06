from tkinter import *
import random

play_board = ['X', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def display_board(board):
    # clean the board and display a new one
    for i in range(1, 9, 3):
        print(board[i:i+3])
    print("\n" * 4)


def player_input():
    # if the player input is X or O return the player input
    player_1 = input("Please pick a marker 'X' or 'O' \n").upper()
    player_2 = "X"
    if player_1 == 'X':
        player_2 = "O"
        print("Player 1 play as " + player_1, ", player 2 play as " + player_2)
        return [player_1, player_2]
    elif player_1 == 'O':
        print("Player 1 play as " + player_1, ", player 2 play as " + player_2)
        return [player_1, player_2]
    else:
        print('\x1b[1;31;0m' + "Invalid input, try again!" + '\x1b[0m')
        playerL = player_input()
    return playerL


def place_marker(board, marker, position):
    # add to the board list a marker in the position input
    if space_check(board, position):
        board.pop(position)
        board.insert(position, marker)
        return board
    print("This position is full, try another")
    position = player_choice(board)
    board = place_marker(board, marker, position)
    return board

def win_check(board, marker):
    # check if there is a winner
    marker_l = [marker, marker, marker]
    for i in range(1, 9, 3):
        if board[i:i+3] == marker_l:
            return True
    for i in range(1, 4):
        if board[i::3] == marker_l:
            return True
    if board[1::4] == marker_l or board[3:8:2] == marker_l:
        return True
    return False


def choose_first(player_l):
    first = random.choice(player_l)
    print("the first player to play is " + first)
    return first


def space_check(board, position):
    # check if there is a free space on board
    if board[position].isdigit():
        return True
    return False


def full_board_check(board):
    # check if the board is full of X and O
    for i in board:
        if i.isdigit():
            return False
    return True


def player_choice(board):
    # ask the player where he wants to drop his marker ant return his choice
    print("What is your next move, enter a number between (1 - 9).")
    try:
        choice = int(input())
    except:
        print('\x1b[1;31;0m' + "Invalid position, enter a position (1-9)" + '\x1b[0m')
        choice = player_choice(board)
    if choice in range(1, 10):
        if space_check(board, choice):
            return choice
    else:
        print('\x1b[1;31;0m' + "Invalid position, enter a position (1-9)" + '\x1b[0m')
        choice = player_choice(board)
    return choice

def replay():
    # ask the players if they want another game and return True if yes
    print("Are you want a replay?\n'Y' for Yes or 'N' for No")
    replay = input().upper()
    if replay == "Y":
        return True
    elif replay == "N":
        return False
    print('\x1b[1;31;0m' + "Invalid input, type Y or N" + '\x1b[0m')
    replay()


print("Welcome to Tic Tac Toe!")
flag = True
while True:
    play_board = ['X', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_list = player_input()
    player_1 = player_list[0]
    player_2 = player_list[1]
    first_player = choose_first(player_list)
    second_player = player_2
    if first_player == player_2:
        second_player = player_1
    while flag:
        # first player turn
        display_board(play_board)
        position = player_choice(play_board)
        place_marker(play_board, first_player, position)
        if win_check(play_board, first_player):
            display_board(play_board)
            print('\x1b[1;32;0m' + "The winner is " + first_player + '\x1b[0m')
            flag = False
            break
        if full_board_check(play_board):
            flag = False
            print("The board is full, game over")
            break
        # second player turn
        display_board(play_board)
        position = player_choice(play_board)
        place_marker(play_board, second_player, position)
        if win_check(play_board, second_player):
            print("The winner is " + second_player)
            flag = False
    if not replay():
        break
    flag = True
