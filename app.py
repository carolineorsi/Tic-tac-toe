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
    first_player = request.args.get('first-player')
    
    if first_player == 'random':
        player_opts = ['user', 'computer']
        first_player = random.choice(player_opts)

    if first_player == 'computer':
        board = [i for i in range(10)]
        board[4] = 'X'
        return jsonify(board=board,
                       message='Computer went first. Your turn.')

    else:
        return jsonify(message='You go first.')


@app.route('/game')
def play_game():

    return jsonify(message='Computer Played')



if __name__ == '__main__':
    app.run(debug=True)