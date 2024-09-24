from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import re as re

data = {"10" : "Привет мир"}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Салама-лексус {update.effective_user.first_name}\nКомандочки ботика:')
app = ApplicationBuilder().token("7048375689:AAGGQM9GAPrf4w4vlGWMc3dbX5d_24yNm70").build()

async def get(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    art = re.findall(r'\".*?\"', update.message.text)
    if len(art) != 1 :
        await update.message.reply_text("Gang!")
        return
    code = art[0].replace('"',"")
    await update.message.reply_text(data[code])
app = ApplicationBuilder().token("7048375689:AAGGQM9GAPrf4w4vlGWMc3dbX5d_24yNm70").build()

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    art = re.findall(r'\".*?\"', update.message.text)
    if len(art) != 2 :
        await update.message.reply_text("Gang!")
        return
    code = re.findall(r'\".*?\"', update.message.text)[0].replace('"',"")
    message = re.findall(r'\".*?\"', update.message.text)[1].replace('"',"")
    data[code] = message
    await update.message.reply_text("ОК!")
app = ApplicationBuilder().token("7048375689:AAGGQM9GAPrf4w4vlGWMc3dbX5d_24yNm70").build()
    
app.add_handler(CommandHandler("Start", start))
app.add_handler(CommandHandler("Set", add))
app.add_handler(CommandHandler("Get", get))
app.run_polling()