import telebot
from threading import Thread

token = '1124773149:AAHh1EpBNC5ZYeNrGwhFMGpQa9WASTUycys'
bot = telebot.TeleBot(token)

# Greeting message
@bot.message_handler(commands=["start"])
def greet(message):
    bot.send_message(message.chat.id, "Приветствую! Я — бот, который поможет тебе подготовиться к ЕГЭ. Для начала выбери, какой предмет тебя интересует.")
    # Здесь было бы неплохо предложить пользователю кнопки для выбора предмета.

# Continiously updating for new incoming messages
def update_messages():
    bot.polling(none_stop=True)

polling = Thread(target=update_messages)
polling.start()

# Text messages processing
@bot.message_handler(content_types=["text"])
def answer(message):
    income = message.text.lower()
    if "привет" in income:
        result = "И тебе привет! Что ты хочешь узнать?"
    elif "как дела" in income:
        result = "У меня всё хорошо, и я, как всегда, готов тебе помочь!"
    elif "не понимаю" in income or "не понятно" in income or "непонятно" in income:
        result = "Что именно непонятно? Задай конкретный вопрос, и тогда я смогу помочь."
    elif "помоги" in income:
        result = "Уточни, пожалуйста, чем именно я могу тебе помочь."
    else:
        result = "К сожалению, я не понимаю твой вопрос. Повтори, пожалуйста, на понятном мне языке."
    # Sending message
    bot.send_message(message.chat.id, result)
