from email import message
from multiprocessing.reduction import send_handle
import webbrowser
import telebot
from telebot import *

bot=telebot.TeleBot("6861229003:AAGL9kI7QDofMhXaml2EPHCDuTblb0ooCEI")
fla=False

@bot.message_handler(content_types="photo")
def mas_photo(message):
    bot.reply_to(message, "классное")
    
    
    

@bot.message_handler(commands=["start"])
def main(massge):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("наш сайт", url="https://успокойся.рус"))
    markup.add(types.InlineKeyboardButton("мне скучно", callback_data="как дела?"))
    bot.send_message(massge.chat.id, f"привет! {massge.from_user.first_name}", reply_markup=markup)
    
    
@bot.callback_query_handler(func=lambda callback: True)
def della(callback):
    bot.register_next_step_handler(bot.send_message(callback.message.chat.id, "как твои дела?"), otv)


def otv(message):
    if message.text.lower()=="плохо":
        bot.send_message(message.chat.id, "К сожалению могу только пожелать удачи, надеюсь у тебя будет все хорошо🥺")
    if message.text.lower()=="хорошо":
        bot.send_message(message.chat.id, "Это отлично! Очень рад за тебя")
    
    
@bot.message_handler(commands=["new"])
def main(massge):
    bot.send_message(massge.chat.id, "вы теперь с нами!")
    bot.send_message(1511626416, "плюс 1")
    
    
    
@bot.message_handler(commands="helppr")
def main(massage):
    bot.send_message(massage.chat.id, massage)
    
    
    
@bot.message_handler()
def diz(massage):
    if massage.text.lower()=="как дела?":
        bot.send_message(massage.chat.id, "прекрасно")
    
    else:
        bot.send_message(massage.chat.id, "извини не могу помочь(")
        
        
    
bot.polling(non_stop=True)