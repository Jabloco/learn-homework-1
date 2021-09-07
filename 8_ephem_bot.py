"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import settings
import datetime
from ephem import *

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    user_text_list = user_text.split()
    if user_text_list[0] == '/planet':
        update.message.reply_text(planet(user_text_list[1].lower()))
    else:
        print(user_text)
        update.message.reply_text(user_text)

def planet(input_planet):
    if input_planet == 'mercury':
        return constellation(Mercury(datetime.date.today()))[1]
    elif input_planet == 'venus':
        return constellation(Venus(datetime.date.today()))[1]
    elif input_planet == 'mars':
        return constellation(Mars(datetime.date.today()))[1]
    elif input_planet == 'jupiter':
        return constellation(Jupiter(datetime.date.today()))[1]
    elif input_planet == 'saturn':
        return constellation(Saturn(datetime.date.today()))[1]
    elif input_planet == 'uranus':
        return constellation(Uranus(datetime.date.today()))[1]
    elif input_planet == 'neptune':
        return constellation(Neptune(datetime.date.today()))[1]
    else:
        return 'Я не знаю такой планеты'
    

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
