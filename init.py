import telebot

bot = telebot.TeleBot('6063552257:AAEFuTPvYRiaHf_Z4-SEhchVkS_uQMkSU3w')


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, '123')


bot.polling(none_stop=True)
