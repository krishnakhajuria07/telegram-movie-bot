from pyrogram import Client, filters
from config import *

app = Client(
    "MovieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    await message.reply("✅ Bot is working!")

app.run()
