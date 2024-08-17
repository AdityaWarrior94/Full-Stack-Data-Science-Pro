import requests
from telegram.ext import Updater, CommandHandler

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Function to handle the /start command
def start(bot, update):
    update.message.reply_text('Hello! Use /price to get the latest BTC price from Gemini.')

# Function to handle the /price command
def price(bot, update):
    try:
        response = requests.get('https://api.gemini.com/v1/pubticker/btcusd')
        data = response.json()
        current_price = data['last']
        update.message.reply_text(f'The current BTC price on Gemini is: ${current_price}')
    except Exception as e:
        update.message.reply_text(f'An error occurred: {e}')

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", price))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
