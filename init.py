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
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'add':
        bot.send_message(call.message.chat.id, 'Введите слово и перервод через пробел')
        bot.register_next_step_handler(call.message, process_add)
    elif call.data == 'clear':
        process_clear(call.message)
    elif call.data == 'get all':
        process_get_all(call.message)


def process_add(message):
    data = (message.text.split(' '))
    add_word(data[0], data[1])
    bot.send_message(message.chat.id, 'Добавлено!')


def process_clear(message):
    clear()
    bot.send_message(message.chat.id, 'Все слова удалены!')


def process_get_all(message):
    datas = get_words()
    text = ''
    if len(datas) > 0:
        for data in datas:
            text += data.get_text()+'\n'
        bot.send_message(message.chat.id, text)


bot.polling()
