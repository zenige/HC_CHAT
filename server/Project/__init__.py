from flask import Flask


app = Flask(__name__, static_url_path='/static')

from Project.route.bot import bot

app.register_blueprint(bot, url_prefix='/bot')