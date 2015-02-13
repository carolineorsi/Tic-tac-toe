from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)



@app.route('/')
def show_index():
    """ The index page of the site """

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)