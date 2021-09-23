from config import TOKEN
from telegramBot import telegramBot
from parserAnekdot import renderAnekdots

def run():
    confirmParse = input("Do you want to Download or Update data [Y/N] ")
    if confirmParse.lower() == "y" or confirmParse.lower() == 'yes':
        renderAnekdots()
    confirmBot = input("Do you want to on TelegramBot [Y/N]")
    if confirmBot.lower() == "y" or confirmBot.lower() == 'yes':
        telegramBot(TOKEN)
    


if __name__ == '__main__':
    run()




