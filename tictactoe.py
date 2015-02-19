import random

WINNING_COMBOS = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

def set_players(first_player):

    if first_player == 'random':
            player_opts = ['user', 'computer']
            random.shuffle(player_opts)

            first_player = player_opts.pop()

    if first_player == 'computer':
        return {'X':'computer', 'O':'user'}
    else:
        return {'X':'user', 'O':'computer'}


def check_winner(board):
    """ Checks all possible winning combinations for winner. """

    for combo in WINNING_COMBOS:
        player = board[combo[0]]
        if board[combo[1]] == player and board[combo[2]] == player:
            return player

    return None


def check_possible_win(board):
    available = []
    matches = []

    for combo in WINNING_COMBOS:
        for square in combo:




def is_available(board, square):
    return board[square] == square