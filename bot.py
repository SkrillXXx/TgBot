from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import re as re
import sqlalchemy as db

data = {"10" : "Привет мир"}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Салама-лексус {update.effective_user.first_name}\nКомандочки ботика:\n/get\n/add\n/gets\n/sets')
app = ApplicationBuilder().token("7048375689:AAGGQM9GAPrf4w4vlGWMc3dbX5d_24yNm70").build()

async def get(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    art = re.findall(r'\".*?\"', update.message.text)
    if len(art) != 1 :
        await update.message.reply_text("Gang!")
        return
    code = art[0].replace('"',"")
    await update.message.reply_text(data[code])
app = ApplicationBuilder().token("7048375689:AAGGQM9GAPrf4w4vlGWMc3dbX5d_24yNm70").build()

async def anime(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass

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

async def get_anime(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    art = update.message.text.split(" ")
    id = int(art[1])
    engine = db.create_engine("mysql+pymysql://root@127.0.0.1/Anime?charset=utf8mb4")
    kast = engine.connect()
    query = db.text(f"SELECT * FROM anime1 WHERE id = {id}")
    anime = kast.execute(query).fetchall()
    await update.message.reply_text(str(anime[0][0])+ str("\n\n")+ str(anime[0][1]))

async def set_anime(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    art = update.message.text.split(" ")
    id = int(art[1]) # Получение id из сообщения
    new_name = art[2]   # Получение нового имени аниме из сообщения (в качестве примера)
    engine = db.create_engine("mysql+pymysql://root@127.0.0.1/Anime?charset=utf8mb4")
    kast = engine.connect()
    query = db.text(f"INSERT INTO anime1 (name,description) VALUES('{id}','{new_name}')")  # Создание запроса на обновление
    kast.execute(query) # Выполнение запроса
    kast.commit()
    await update.message.reply_text(f"ДОБАВИЛИ НОВУЮ АНИМЕ.")
    



    
app.add_handler(CommandHandler("Start", start))
app.add_handler(CommandHandler("Set", add))
app.add_handler(CommandHandler("Get", get))
app.add_handler(CommandHandler("Gets", get_anime))
app.add_handler(CommandHandler("Sets", set_anime))
app.run_polling()
