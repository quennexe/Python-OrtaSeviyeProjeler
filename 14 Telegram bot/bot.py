from telegram.ext import Updater, CommandHandler

# BOT TOKENINI BURAYA EKLEYİN
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("Merhaba! Ben basit bir Telegram botuyum. ✨")

def help_command(update, context):
    update.message.reply_text("Komutlar:\n/start - Başlat\n/help - Yardım")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    print("Bot çalışıyor... Telegram'da komut gönderin.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
