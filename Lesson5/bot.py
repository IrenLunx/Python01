from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
print('Все ок!')

app = ApplicationBuilder().token("5183281373:AAEBiRZGgZdMxYjNrvwacj6sUpr1b1CD_Oc").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()