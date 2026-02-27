import telebot
from telebot import types
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("💳 Оплата 370₽", callback_data="pay1")
    btn2 = types.InlineKeyboardButton("💳 Оплата 260₽", callback_data="pay2")
    btn3 = types.InlineKeyboardButton("🧪 Тест сервера", callback_data="test")
    btn4 = types.InlineKeyboardButton("👤 Связь с админом", url="https://t.me/Vip_kanal_TVV")

    markup.add(btn1, btn2)
    markup.add(btn3)
    markup.add(btn4)

    bot.send_message(message.chat.id,
                     "📡 Добро пожаловать в VIP TV\n\nВыберите действие:",
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "pay1":
        bot.send_message(call.message.chat.id,
                         "💳 Оплата 370₽\n\nПосле оплаты отправьте скрин администратору.")

    elif call.data == "pay2":
        bot.send_message(call.message.chat.id,
                         "💳 Оплата 260₽\n\nПосле оплаты отправьте скрин администратору.")

    elif call.data == "test":
        bot.send_message(call.message.chat.id,
                         "🧪 Тестовый плейлист:\nhttps://example.com/test.m3u")

bot.infinity_polling()
