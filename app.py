from flask import Flask, request, render_template, redirect, url_for, jsonify
import random
# import tictactoe

app = Flask(__name__)

@app.route('/')
def show_index():
    """ The index page of the site """

    return render_template('index.html')


@app.route('/game')
def start_game():
    first_player = request.args.get('first-player')
    
    if first_player == 'random':
        player_opts = ['user', 'computer']
        first_player = random.choice(player_opts)

    if first_player == 'computer':
        return render_template('index.html', board=[0,1,2,3,'X',5,6,7,8])
    else:
        return 'Player goes first'



if __name__ == '__main__':
    app.run(debug=True)