import telebot
from telebot import types
from Presenter import get_words, clear_words, add_word, get_literatures, add_literature, \
    clear_literatures

bot = telebot.TeleBot('6063552257:AAEFuTPvYRiaHf_Z4-SEhchVkS_uQMkSU3w')


@bot.message_handler(commands=['start'], content_types=['text'])
def start(message):
    bot.send_message(message.chat.id,
                     'Бот создан для помощи в изучении иностранных языков')


@bot.message_handler(commands=['words'], content_types=['text'])
def words(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Новое слово', callback_data='add word')
    button2 = types.InlineKeyboardButton(text='Список', callback_data='get all words')
    button3 = types.InlineKeyboardButton(text='Очистить все', callback_data='clear words')
    markup.row(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)


@bot.message_handler(commands=['literatures'], content_types=['text'])
def literatures(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Новая литература',
                                         callback_data='add literature')
    button2 = types.InlineKeyboardButton(text='Список литературы',
                                         callback_data='get all literatures')
    button3 = types.InlineKeyboardButton(text='Очистить все',
                                         callback_data='clear literatures')
    markup.row(button1, button2, button3)
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'add word':
        bot.send_message(call.message.chat.id, 'Введите слово и перевод через пробел')
        bot.register_next_step_handler(call.message, process_add_word)
    elif call.data == 'clear words':
        process_clear_words(call.message)
    elif call.data == 'get all words':
        process_get_all_words(call.message)
    elif call.data == 'add literature':
        bot.send_message(call.message.chat.id,
                         'Введите название, автора и ссылку через запятую')
        bot.register_next_step_handler(call.message, process_add_literatures)
    elif call.data == 'clear literatures':
        process_clear_literatures(call.message)
    elif call.data == 'get all literatures':
        process_get_all_literatures(call.message)


def process_add_word(message):
    data = (message.text.split(' '))
    if len(data) != 2:
        bot.send_message(message.chat.id, 'Необходимо ввести 2 слова через пробел')
        return
    add_word(data[0], data[1])
    bot.send_message(message.chat.id, 'Добавлено!')


def process_clear_words(message):
    clear_words()
    bot.send_message(message.chat.id, 'Все слова удалены!')


def process_get_all_words(message):
    datas = get_words()
    text = ''
    if len(datas) > 0:
        for data in datas:
            text += data.get_text()+'\n'
        bot.send_message(message.chat.id, text)


def process_add_literatures(message):
    data = (message.text.split(', '))
    if len(data) != 3:
        bot.send_message(message.chat.id,
                         'Необходимо ввести название, автора и ссылку через запятую')
        return
    add_literature(data[0], data[1], data[2])
    bot.send_message(message.chat.id, 'Добавлено!')


def process_clear_literatures(message):
    clear_literatures()
    bot.send_message(message.chat.id, 'Вся литература удалена!')


def process_get_all_literatures(message):
    datas = get_literatures()
    text = ''
    if len(datas) > 0:
        for data in datas:
            info, link = data.get_text()
            text += info+', [Ссылка]('+link+')'+'\n\n'
        bot.send_message(message.chat.id, text, parse_mode="MarkdownV2")


bot.polling()
