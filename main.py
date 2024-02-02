import os
from os import getenv
import logging
from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import ChatAdminRequired


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(filters.command("banall") & filters.group)
async def banall(client, message):
    print("getting memebers from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id,message.chat.id))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print("failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")

# start client
app.start()
print("Bot Started")
idle()
