from flask import Flask, request, abort, render_template, session,url_for,redirect,send_from_directory,send_file,Blueprint,current_app

bot = Blueprint("bot",__name__)

@bot.route('/', methods=['GET', 'POST'])
def history():
    return "True"