import os
import telebot
from telebot import types

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# стартова команда
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("1", callback_data="1"),
        types.InlineKeyboardButton("2", callback_data="2"),
        types.InlineKeyboardButton("3", callback_data="3")
    )
    bot.send_message(message.chat.id, "Вибери цифру:", reply_markup=markup)

# обробка натискань
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data in ["1", "2", "3"]:
        markup = types.InlineKeyboardMarkup()
        for i in range(1, 4):
            markup.add(types.InlineKeyboardButton(f"{call.data}{i}", callback_data=f"{call.data}{i}"))
        bot.edit_message_text(
            f"Ти вибрав {call.data}. Обери далі:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )
    elif len(call.data) == 2:
        bot.send_message(call.message.chat.id, f"Ти вибрав фінальний варіант: {call.data}")

bot.polling(non_stop=True)
