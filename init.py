import telebot
from telebot import types
from Presenter import get_words, clear, add_word

bot = telebot.TeleBot('6063552257:AAEFuTPvYRiaHf_Z4-SEhchVkS_uQMkSU3w')


@bot.message_handler(commands=['start'], content_types=['text'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Новое слово', callback_data='add')
    button2 = types.InlineKeyboardButton(text='Список', callback_data='get all')
    button3 = types.InlineKeyboardButton(text='Очистить все', callback_data='clear')
    markup.row(button1, button2, button3)
    bot.send_message(message.chat.id, 'start', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'add':
        bot.send_message(call.message.chat.id, 'Введите слово и перервод через пробел')
        bot.register_next_step_handler(call.message, process_add)


def process_add(message):
    data = (message.text.split(' '))
    add_word(data[0], data[1])
    bot.send_message(message.chat.id, 'Добавлено!')


bot.polling()
