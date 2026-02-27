import telebot
from telebot import types
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)


# ==============================
# ГЛАВНАЯ СТРАНИЦА
# ==============================
@bot.message_handler(commands=['start'])
def start(message):
    send_main_page(message.chat.id)


def send_main_page(chat_id):

    text = "📡 *VIP IPTV & Плагины* 📺\n\nВыберите раздел 👇"

    markup = types.InlineKeyboardMarkup()

    markup.row(
        types.InlineKeyboardButton("⭐ Премиум Плагин Lampa 4K", callback_data="plugin_page")
    )

    markup.row(
        types.InlineKeyboardButton("💳 Оплата IPTV", url="https://evgeshkawww.github.io/iptv/IPTV/index.html")
    )

    with open("iptv.jpeg", "rb") as photo:
        bot.send_photo(
            chat_id,
            photo,
            caption=text,
            parse_mode="Markdown",
            reply_markup=markup
        )


# ==============================
# ВТОРАЯ СТРАНИЦА (ПЛАГИН)
# ==============================
def send_plugin_page(chat_id):

    text = (
        "⭐ *Премиум Плагин Lampa 4K*\n\n"
        "💰 Стоимость:\n"
        "• 1 месяц — *250₽*\n"
        "• 2 месяца и более — *210₽ в месяц*\n\n"
        "📱 Можно использовать на *3 устройствах*\n\n"
        "После оплаты квитанцию отправить Админу.\n"
        "Далее мы подключаем Вас и выдаем бота,\n"
        "где Вы получаете ссылку.\n\n"
        "Там есть инструкция по настройке\n"
        "и наша версия приложения Lampa\n"
        "для корректной работы плагинов.\n\n"
        "Выбирайте удобный способ оплаты.\n"
        "Хорошего дня! ☀"
    )

    markup = types.InlineKeyboardMarkup()

    markup.row(
        types.InlineKeyboardButton(
            "💳 Перейти к оплате",
            url="https://evgeshkawww.github.io/iptv/IPTV/index.html"
        )
    )

    markup.row(
        types.InlineKeyboardButton("⬅ Назад", callback_data="back_main")
    )

    bot.send_message(
        chat_id,
        text,
        parse_mode="Markdown",
        reply_markup=markup
    )


# ==============================
# ОБРАБОТКА КНОПОК
# ==============================
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    if call.data == "plugin_page":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_plugin_page(call.message.chat.id)

    elif call.data == "back_main":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_main_page(call.message.chat.id)


bot.infinity_polling()
