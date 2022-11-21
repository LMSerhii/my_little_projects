
import requests
from datetime import datetime
from auth_data import token
import telebot


def get_data():
    req = requests.get("https://btc-trade.com.ua/api/ticker/btc_uah")
    response = req.json()
    sell_price = response['btc_uah']['sell_usd']
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

def telegramm_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! Write the 'price'"
                                          " to find out the cost of BTC!" )

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://btc-trade.com.ua/api/ticker/btc_uah")
                response = req.json()
                sell_price = response['btc_uah']['sell_usd']
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn ... Something was wrong..."
                    )
        else:
            bot.send_message(message.chat.id, "Whaaat??? Check the command dude! ")


    bot.polling()

if __name__ == "__main__":
    get_data()
    telegramm_bot(token)