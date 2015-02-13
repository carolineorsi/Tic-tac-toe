import random

def choose_player():
    players = ['user', 'computer']
    random.shuffle(players)

    players = {'X': players.pop(), 'O': players.pop()}

    return players


def check_winner(board):
    winning_combos = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for combo in winning_combos:
        player = board[combo[0]]
        if board[combo[1]] == player and board[combo[2]] == player:
            return player

    return None