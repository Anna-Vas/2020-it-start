import telebot

token = '1337'  # Replace 1337 with your telegram bot token
bot = telebot.TeleBot(token)

# Greeting message
@bot.message_handler(commands=["start"])
def start_spam(message):
    bot.send_message(message.chat.id, "Hey! I'm a really simple chat bot.")
users = []

# Continiously updating for new incoming messages
def update_messages():
    bot.polling(none_stop=True)

# Text messages processing
@bot.message_handler(content_types=["text"])
def answer(message):
    # Python code executing
    try:
        result = eval(message.text)
    # Common answer for all other messages
    except Exception as e:
                result = "I don't understand you. Set a valid command."
    # Sending message
    bot.send_message(message.chat.id, result)