from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,MessageHandler , ContextTypes, filters

BOT_TOKEN = "TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salam, in task man hast baraye Python Developer, Khosh Amadid!")


async def messagehandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(user_message)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

filter_for_text = filters.TEXT & (~filters.COMMAND)
app.add_handler(MessageHandler(filter_for_text, messagehandler))

app.run_polling()
