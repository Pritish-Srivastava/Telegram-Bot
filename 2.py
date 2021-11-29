from telegram import *
from telegram.ext import *

# bot = Bot("-------------------")                can't tell telegram bot token code for obvious reason

# updater=Updater("-----------------------------")

dispatcher=updater.dispatcher

def test_function(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="Heyyyyyy",
        )

start_value=CommandHandler('hi',test_function)

dispatcher.add_handler(start_value)


def test_function1(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="Everything is fine,what about you?",
        )

start_value1=CommandHandler('wassup',test_function1)

dispatcher.add_handler(start_value1)

def test_function2(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="No i am dead lol",
        )

start_value2=CommandHandler('are_you_alive',test_function2)

dispatcher.add_handler(start_value2)

def test_function3(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="Pritish & Sondarya i guess lol",
        )

start_value3=CommandHandler('who_made_you',test_function3)

dispatcher.add_handler(start_value3)

def test_function4(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="Becky",
        )

start_value4=CommandHandler('whats_your_name',test_function4)

dispatcher.add_handler(start_value4)

def test_function5(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="While playing squid game,i died!",
        )

start_value5=CommandHandler('How_did_you_died',test_function5)

dispatcher.add_handler(start_value5)

def test_function6(update:Update,context:CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text="who ask dead person their age xD",
        )

start_value6=CommandHandler('Whats_your_age',test_function6)

dispatcher.add_handler(start_value6)


print(bot.get_me())

updater.start_polling()