import telebot

from flask import Flask, request

import os

app = Flask(__name__)

bot = telebot.TeleBot("6244126708:AAF-8_qFjbs2tuyTwZQ9iVpAduLnBX6t_iE")

@app.route('/' + bot.token, methods=['POST'])

def handle_updates():

    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))

    bot.process_new_updates([update])

    return "OK"

@app.route('/')

def index():

    return "Hello, this is your Flask app!"

@bot.message_handler(commands=['start'])

def send_welcome(message):

    bot.reply_to(message, "Hello, welcome to my bot!")

@bot.message_handler(commands=['help'])

def send_help(message):

    bot.reply_to(message, "Here are some commands you can use:\n/start - say hello\n/help - get help")

@bot.message_handler(func=lambda message: True)

def echo_all(message):

    bot.reply_to(message, message.text)

bot.remove_webhook()

bot.set_webhook(url='https://abcde-ml9iz4qi5-becaalemu-gmailcom.vercel.app/' + bot.token)

if __name__ == '__main__':

    app.run(debug=True, port=int(os.environ.get('PORT', 5000)), host='0.0.0.0')













      




