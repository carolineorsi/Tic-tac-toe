from flask import Flask, request, render_template, redirect, url_for, jsonify
import random
# import tictactoe

app = Flask(__name__)

@app.route('/')
def show_index():
    """ The index page of the site """

    return render_template('index.html')


@app.route('/random')
def choose_player():
    players = ['user', 'computer']
    first = random.choice(players)

    return first


if __name__ == '__main__':
    app.run(debug=True)