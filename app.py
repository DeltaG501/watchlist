from flask import Flask
app = Flask(__name__)


@app.route('/user/<name>')
def hello(name):
    return "<h1>Welcome to %s's watchlist</h1>" % name
