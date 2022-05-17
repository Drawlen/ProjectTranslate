import telebot
import requests
import random

from telebot import types
from googletrans import Translator
from bs4 import BeautifulSoup

translator = Translator()

bot = telebot.TeleBot('5340373499:AAHqOE2bXJ7_-mYloTO4oKat_tmySpgNG0s')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'<i>Привет, <b>{message.from_user.first_name}</b>, я бот для перевода и рассылки текста</i>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    translate = types.KeyboardButton('🇺🇸Перевести🇷🇺')
    translate2 = types.KeyboardButton('🇷🇺Перевести🇺🇸')
    new = types.KeyboardButton('✨Случайный набор✨')
    inform = types.KeyboardButton('🔸Информация🔸')
    nast = types.KeyboardButton('⚙️Настройки⚙️')

    markup.add(translate, translate2, new, inform, nast)
    messa = f'<i>Список доступных вам возможностей</i>'
    bot.send_message(message.chat.id, messa, reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.chat.type == 'private':
        if message.text == '🇺🇸Перевести🇷🇺':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            back = types.KeyboardButton('⬅️Назад')
            markup.add(back)
            msgs = bot.send_message(message.chat.id, '<i>🇺🇸Введите текст для перевода🇷🇺</i>', reply_markup=markup, parse_mode='html')
            bot.register_next_step_handler(msgs, some_1)


        elif message.text == '⚙️Настройки⚙️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            kolvo = types.KeyboardButton('♾Количество слов♾')
            chast = types.KeyboardButton('🕰Частота🕰')
            back = types.KeyboardButton('⬅️Прошлое меню')
            markup.add(kolvo, chast, back)
            bot.send_message(message.chat.id, '<i>⛔️Меню настроек не функционирует⛔️</i>', reply_markup=markup, parse_mode='html')

        elif message.text == '✨Случайный набор✨':
            bot.send_message(message.chat.id, "<i>✨Генерирую случайный набор слов...✨</i>", parse_mode='html')
            url = 'https://kreekly.com/random//'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            items = soup.find_all('div', class_='dict-word')

            for n, i in enumerate(items, start=1):
                itemEng = i.find('span', class_='eng').text.strip()
                itemRus = i.find('span', class_='rus').text

                bot.send_message(message.chat.id, (f'{n}. {itemEng} - {itemRus}'))


        elif message.text == '🔸Информация🔸':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            obote = types.KeyboardButton('🌆О боте🌃')
            what = types.KeyboardButton('🗿А это для чего?🗿')
            back = types.KeyboardButton('⬅️Прошлое меню')
            markup.add(obote, what, back)
            bot.send_message(message.chat.id, '<i>🔸Информационное меню🔸</i>', reply_markup=markup, parse_mode='html')

        elif message.text == '🌆О боте🌃':
            mesage = f'<i>Главным функционалом этого бота на данный момент является перевод текста, а также генерация различных иностанных слов и словосочетаний</i>'
            bot.send_message(message.chat.id, mesage, parse_mode='html')
            mesag = f'<i>В будущем появится функция регистрации и ежедневной расслыки иностранных слов/словосочетаний (которые также будут включать их перевод), с возможностью настройки количества отправляемых слов, а также частоты, с которой они будут отправляться в течении дня (например, одно слово - один раз в день, или по два слова - три раза в день)</i>'
            bot.send_message(message.chat.id, mesag, parse_mode='html')

        elif message.text == '🗿А это для чего?🗿':
            bot.send_message(message.chat.id, 'О, повезло повезло')
            bot.send_message(message.chat.id, str(random.randint(0, 1)))

        elif message.text == '⬅️Прошлое меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            translate = types.KeyboardButton('🇺🇸Перевести🇷🇺')
            translate2 = types.KeyboardButton('🇷🇺Перевести🇺🇸')
            new = types.KeyboardButton('✨Случайный набор✨')
            inform = types.KeyboardButton('🔸Информация🔸')
            nast = types.KeyboardButton('⚙️Настройки⚙️')
            markup.add(translate, translate2, new, inform, nast)
            messa = f'<i><b>✖️Главное меню✖️</b></i>'
            bot.send_message(message.chat.id, messa, reply_markup=markup, parse_mode='html')

        elif message.text == '🇷🇺Перевести🇺🇸':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            back = types.KeyboardButton('⬅️Назад')
            markup.add(back)
            msgs = bot.send_message(message.chat.id, '<i>🇷🇺Введите текст для перевода🇺🇸</i>', reply_markup=markup, parse_mode='html')
            bot.register_next_step_handler(msgs, some_2)


def some_2(message):
        if message.text == '⬅️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            translate = types.KeyboardButton('🇺🇸Перевести🇷🇺')
            translate2 = types.KeyboardButton('🇷🇺Перевести🇺🇸')
            new = types.KeyboardButton('✨Случайный набор✨')
            inform = types.KeyboardButton('🔸Информация🔸')
            nast = types.KeyboardButton('⚙️Настройки⚙️')
            markup.add(translate, translate2, new, inform, nast)
            messa = f'<i><b>✖️Главное меню✖️</b></i>'
            bot.send_message(message.chat.id, messa, reply_markup=markup, parse_mode='html')

        elif message.text == message.text:
            translator = Translator()
            t = (translator.translate(message.text, src="ru", dest="en"))
            txt = bot.send_message(message.chat.id, t.text)
            bot.register_next_step_handler(txt, some_2)

def some_1(message):

    if message.text == '⬅️Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        translate = types.KeyboardButton('🇺🇸Перевести🇷🇺')
        translate2 = types.KeyboardButton('🇷🇺Перевести🇺🇸')
        new = types.KeyboardButton('✨Случайный набор✨')
        inform = types.KeyboardButton('🔸Информация🔸')
        nast = types.KeyboardButton('⚙️Настройки⚙️')
        markup.add(translate, translate2, new, inform, nast)
        messa = f'<i><b>✖️Главное меню✖️</b></i>'
        bot.send_message(message.chat.id, messa, reply_markup=markup, parse_mode='html')

    elif message.text == message.text:
        translator = Translator()
        t = (translator.translate(message.text, src="en", dest="ru"))
        txt = bot.send_message(message.chat.id, t.text)
        bot.register_next_step_handler(txt, some_1)

# @bot.message_handler(commands=['Английский'])
# def some_3(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Перевести?'))
#     bot.send_message(message.chat.id, word(min_word_len=5), reply_markup=markup)

bot.polling(none_stop=True)