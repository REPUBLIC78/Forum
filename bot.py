import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Токен вашего бота
TOKEN = '7545479346:AAEdMLhLPO60JR3wiz0GuKPN9QaK7kYz60c'

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
    # Создаем приложение и передаем ему токен
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчик команды /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)


    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(echo_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
