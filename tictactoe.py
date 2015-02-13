import random

def choose_player():
    players = ['user', 'computer']
    random.shuffle(players)

    players = {'X': players.pop(), 'O': players.pop()}

    return players


# def check_winner(board):
