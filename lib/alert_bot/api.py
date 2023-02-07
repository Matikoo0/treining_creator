import telegram

def handle_message(bot, update):
    chat_id = update.message.chat_id
    print("Received message from chat ID:", chat_id)
    # your code here

token = "6059621876:AAH7ydLJ2HH8_mFkxavw4E4NMl2WbkC8KwA"
bot = telegram.Bot(token)
updater = telegram.Update(bot.id)
dispatcher = updater.dispatcher
message_handler = telegram.MessageHandler(telegram.Filters.text, handle_message)
dispatcher.add_handler(message_handler)
updater.start_polling()
