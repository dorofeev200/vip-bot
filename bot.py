import telebot
from telebot import types
import os
import threading
from flask import Flask

# =============================
# TELEGRAM BOT
# =============================

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

# =============================
# WEB SERVER (для Render FREE)
# =============================

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web).start()

# =============================
# ГЛАВНАЯ СТРАНИЦА
# =============================

@bot.message_handler(commands=['start'])
def start(message):
    send_main_page(message.chat.id)

def send_main_page(chat_id):

    def send_main_page(chat_id):

    text = (
        "📡 *Как окунуться в МИР ТЕЛЕВИДЕНИЯ?* 📺\n\n"
        "1️⃣ Нужно определиться какой плей-лист вы хотите?\n"
        "*Премиум или Простой*\n"
        "Оплата от 2-х месяцев *ДЕШЕВЛЕ!!!*\n\n"
        "2️⃣ Пройти Тест Серверов для Премиум телевидения.\n"
        "Для обычного не нужно.\n\n"
        "🔥 При покупке пакета Премиум\n"
        "Плагин Lampa 4K получаете в подарок!\n\n"
        "3️⃣ Сделать скриншот всего теста\n"
        "4️⃣ Оплатить плейлист\n"
        "5️⃣ Квитанцию отправить Админу\n\n"
        "👇 После добавления получите плейлист"
    )

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.row(
        types.InlineKeyboardButton("Оплата",
                                   url="https://evgeshkawww.github.io/iptv/IPTV/index.html"),
        types.InlineKeyboardButton("370Р",
                                   url="https://evgeshkawww.github.io/iptv/IPTV/spisok.html"),
        types.InlineKeyboardButton("260Р",
                                   url="https://evgeshkawww.github.io/iptv/IPTV/wiytiu3.html"),
    )

    markup.row(
        types.InlineKeyboardButton("🧪 Тест Серверов",
                                   url="https://evgeshkawww.github.io/iptv/IPTV/speed_test.html"),
        types.InlineKeyboardButton("🔥 Lampa 4K",
                                   callback_data="plugin_page")
    )

    markup.row(
        types.InlineKeyboardButton("📺 Видео Плей-Листа ВК",
                                   url="https://vkvideo.ru/video-145539285_456240212")
    )

    markup.row(
        types.InlineKeyboardButton("📺 Видео Плей-Листа Rutube",
                                   url="https://rutube.ru/video/8f243e078d480f7422fc023906d1fd6e/?r=wd")
    )

    markup.row(
        types.InlineKeyboardButton("⭐ Премиум Плагин Lampa 4K",
                                   callback_data="plugin_page")
    )

    markup.row(
        types.InlineKeyboardButton("👤 Связь Админ",
                                   url="https://t.me/Vip_kanal_TVV")
    )

    with open("iptv.jpeg", "rb") as photo:
        bot.send_photo(
            chat_id,
            photo,
            caption=text,
            parse_mode="Markdown",
            reply_markup=markup
        )

# =============================
# ВТОРАЯ СТРАНИЦА
# =============================

def send_plugin_page(chat_id):

    text = (
        "⭐ *Премиум Плагин Lampa 4K*\n\n"
        "💰 Стоимость:\n"
        "• 1 месяц — *250₽*\n"
        "• 2 месяца и более — *210₽ в месяц*\n\n"
        "📱 Можно использовать на 3 устройствах.\n\n"
        "После оплаты квитанцию отправить Админу.\n"
        "Далее подключаем Вас и выдаем бота,\n"
        "где получаете ссылку.\n\n"
        "Там есть инструкция по настройке\n"
        "и версия Lampa для корректной работы.\n\n"
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
        types.InlineKeyboardButton("⬅ Назад",
                                   callback_data="back_main")
    )

    bot.send_message(
        chat_id,
        text,
        parse_mode="Markdown",
        reply_markup=markup
    )

# =============================
# CALLBACK
# =============================

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    if call.data == "plugin_page":
        send_plugin_page(call.message.chat.id)

    elif call.data == "back_main":
        send_main_page(call.message.chat.id)

# =============================
# START BOT
# =============================

bot.infinity_polling()
