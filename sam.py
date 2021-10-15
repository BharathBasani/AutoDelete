#👀

import pyrogram
import time

from time import sleep
from pyrogram import Client, filters
from pyrogram.types import User, Message

from info import API_ID
from info import API_HASH
from info import SESSION
from info import ADMINS
from info import TIME

#=======================================================================

Sam = Client(
    session_name= SESSION,
    api_id= API_ID,
    api_hash= API_HASH
)

#=======================================================================

@Sam.on_message(filters.group & filters.all)
def deleter(bot: Client, cmd: Message):
         if cmd.from_user.id not in ADMINS:
                  sleep(int(TIME))
                  cmd.delete()

#=======================================================================

Sam.run()
print("Userbot Started!")

#=======================================================================
