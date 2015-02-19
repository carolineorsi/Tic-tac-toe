from flask import Flask, request, render_template, redirect, url_for, jsonify
import random
import tictactoe

app = Flask(__name__)

@app.route('/')
def show_index():
    """ The index page of the site """

    return render_template('index.html')


@app.route('/start')
def start_game():
    players = tictactoe.set_players(request.args.get('first-player'))
    
    if players['X'] == 'computer':
        board = [i for i in range(10)]
        board[4] = 'X'
        return jsonify(board=board,
                       players=players,
                       message='Computer went first. Your turn.')

    else:
        return jsonify(players=players,
                       message='You go first.')


@app.route('/game')
def play_game():

    return jsonify(message='Computer to play next move...')



if __name__ == '__main__':
    app.run(debug=True)