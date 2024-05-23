import telebot
from config import token
from random import choice

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)


@bot.message_handler(commands=['car'])
def car_maker(message):
    text = message.text
    command, color = text.split(maxsplit=1)

    class Car:
        def __init__(self, color):
            self.color = color
        
    car = Car(color)


    bot.send_message(message.chat.id, f"You made a car with color {car.color}")
    # bot.reply_to(message, message)
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)



bot.infinity_polling()