import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("API_TOKEN")

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context):
    await update.message.reply_text("Здравствуйте")
    logger.info(f"Пользователь {update.message.from_user.username} запустил команду /start")


async def echo(update: Update, context):
    user_message = update.message.text
    logger.info(f"Пользователь {update.message.from_user.username} написал: {user_message}")
    await update.message.reply_text("иди спать")


def main():

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)


    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(echo_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
