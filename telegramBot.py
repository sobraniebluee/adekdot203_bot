from randomAnekdot import randomAnekdot
from config import anekdotsLinks
import telebot

def telegramBot(TOKEN):
    print('BOT STARTED :) ')
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Привет!Нажимай комманду /help и получай долю позитива!")

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.reply_to(message,'Перечень всех комманд: \n\r /anekdothohol - Генерирует Анекдоты про хохлов и москалей \n\r /anekdotbelorusy - Генерирует Анекдоты про белорусов, Беларусь \n\r /anekdotchukcha - Анекдоты про чукчу \n\r /anekdotcygane - Генерирует Анекдоты про цыган \n\r /anekdotevrei - Генерирует Анекдоты про евреев, еврейские \n\r ')

    @bot.message_handler(commands=['anekdothohol'])
    def echo_anekdotHohol(message):
        bot.reply_to(message,randomAnekdot(anekdotsLinks['anekdotHohol'])) 

    @bot.message_handler(commands=['anekdotbelorusy'])
    def echo_anekdotBelorusy(message):
        bot.reply_to(message,randomAnekdot(anekdotsLinks['anekdotBelorusy']))

    @bot.message_handler(commands=['anekdotchukcha'])
    def echo_anekdotChukcha(message):
        bot.reply_to(message,randomAnekdot(anekdotsLinks['anekdotChukcha']))

    @bot.message_handler(commands=['anekdotcygane'])
    def echo_anekdotCygane(message):
        bot.reply_to(message,randomAnekdot(anekdotsLinks['anekdotCygane']))
        
    @bot.message_handler(commands=['anekdotevrei'])
    def echo_anekdotCygane(message):
        bot.reply_to(message,randomAnekdot(anekdotsLinks['anekdotEvrei']))

    bot.polling()
    print('BOT FINISHED! :]')
