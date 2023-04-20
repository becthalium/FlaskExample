from flask import Flask, request
import telebot
app =Flask(__name__ ) 
url="tewvtew"
bot = telebot.TeleBot("6244126708:AAF-8_qFjbs2tuyTwZQ9iVpAduLnBX6t_iE")
bot.remove_webhook()
bot.set_webhook(url=url)
@app.route('/'+secret, methods=['POST'])
def webhook():
      update=telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
      tbot.bot.process_new_updates ([update])
      return 'ok', 200
      
@bot.message_handler(commands=['start']):
	def handle_start(message):
		bot.reply_to(message.from_user.id, "Welcome to the ChatGPT Bot! You have 10 trial messages to use. After that, you'll need to pay for continued usage.")
bot.run()
