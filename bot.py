import telebot
from telebot import types
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):

    text = (
        "📡 *Как окунуться в МИР ТЕЛЕВИДЕНИЯ?*📺\n\n"
        "1️⃣ Нужно определиться какой плей-лист вы хотите для Онлайн ТВ?\n"
        "*Премиум или Простой* ⬜\n"
        "Оплата от 2-х месяцев *ДЕШЕВЛЕ!!!*\n\n"
        "2️⃣ Пройти Тест Серверов для *Премиум телевидения* "
        "чтобы выявить лучший для Вас сервер! ⬜ "
        "Для Обычного не нужно!\n\n"
        "🔥 *Новинка!!!* При покупке пакета *Премиум Плагин Lampa 4K* "
        "получаете в *Подарок!!!*\n\n"
        "3️⃣ Сделать скриншот *Всего Теста (таблицы)* "
        "и прислать Админу для проверки и подтверждения что он у вас будет хорошо работать.\n\n"
        "4️⃣ Оплата плейлиста\n\n"
        "5️⃣ Квитанцию после оплаты предоставить *Админу*\n\n"
        "6️⃣ После Вас добавим в группу и в личные сообщения скинем Плейлист 👇"
    )

    markup = types.InlineKeyboardMarkup(row_width=2)

    # Первый ряд
    markup.add(
        types.InlineKeyboardButton("Оплата", url="https://evgeshkawww.github.io/iptv/IPTV/index.html"),
        types.InlineKeyboardButton("370Р", url="https://evgeshkawww.github.io/iptv/IPTV/spisok.html"),
        types.InlineKeyboardButton("260Р", url="https://evgeshkawww.github.io/iptv/IPTV/wiytiu3.html")
    )

    # Второй ряд
    markup.add(
        types.InlineKeyboardButton("🧪 Тест Серверов", url="https://evgeshkawww.github.io/iptv/IPTV/speed_test.html"),
        types.InlineKeyboardButton("🔥 Lampa 4K", url="https://evgeshkawww.github.io/iptv/IPTV/index.html")
    )

    # Остальные кнопки по одной строке
    markup.add(
        types.InlineKeyboardButton("📺 Видео Плей-Листа!! ВК", url="https://vkvideo.ru/video-145539285_456240212")
    )

    markup.add(
        types.InlineKeyboardButton("📺 Видео Плей-Листа!! Рутуб", url="https://rutube.ru/video/8f243e078d480f7422fc023906d1fd6e/?r=wd")
    )

    markup.add(
        types.InlineKeyboardButton("⭐ Премиум Плагин Lampa 4K", url="https://evgeshkawww.github.io/iptv/IPTV/kino.html")
    )

    markup.add(
        types.InlineKeyboardButton("👤 Связь Админ", url="https://t.me/Vip_kanal_TVV")
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup
    )


bot.infinity_polling()
