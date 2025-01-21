import random
import logging
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command."""
    welcome_message = (
        "🎉 Welcome to FlipBot! 🎲\n"
        "Use the following commands:\n"
        "- /coin: Flip a coin.\n"
        "- /help: Get the list of commands."
    )
    await update.message.reply_text(welcome_message, parse_mode=ParseMode.HTML)

async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /coin command."""
    result = "⚫️ Face" if random.randint(1, 2) == 1 else "⚪️ Cross"
    await update.message.reply_text(f"The coin landed on: {result}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command."""
    help_message = (
        "Available commands:\n"
        "- /start: Start the bot and see a welcome message.\n"
        "- /coin: Flip a coin and get a random result.\n"
        "- /help: See this help message."
    )
    await update.message.reply_text(help_message)

async def error_callback(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error('Update caused an error: %s', context.error)
    if update and isinstance(update, Update) and update.message:
        await update.message.reply_text(
            "⚠️ An error occurred. Please try again later."
        )

def main() -> None:
    """Start the bot."""
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    TOKEN = "YOUR_TOKEN_HERE"

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("coin", coin))
    application.add_handler(CommandHandler("help", help_command))

    application.add_error_handler(error_callback)

    application.run_polling()

if __name__ == "__main__":
    print("[FlipBot] Starting...")
    main()
