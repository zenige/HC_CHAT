from flask import Flask


app = Flask(__name__, static_url_path='/static')

from Project.route.bot import bot
from Project import app


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/images')
def ddd():
    return "A"




if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run( port=5000,debug=True)     