from TeamTeleRoid.database import db
from configs import Config
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("connect") & filters.chat(Config.BOT_OWNER) & filters.private)
async def connnect_group(c: Client, m: Message):

    if len(m.command) == 1:
        return await m.reply('Command Usage: /connect group_id')
    
    if len(m.command) == 2:

        group_id=m.command[1]

        if await db.get_group(group_id):
            return await m.reply('Gʀᴏᴜᴘ Aʟʀᴇᴀᴅʏ Cᴏɴɴᴇᴄᴛᴇᴅ')
        else:
            await db.connect(group_id=group_id)
            return await m.reply('Gʀᴏᴜᴘ ᴄᴏɴɴᴇᴄᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ')



@Client.on_message(filters.command("disconnect") & filters.chat(Config.BOT_OWNER) & filters.private)
async def disconnnect_group(c: Client, m: Message):

    if len(m.command) == 1:
        return await m.reply('Command Usage: /disconnect group_id')
    
    if len(m.command) == 2:

        group_id=m.command[1]

        if await db.get_group(group_id):
            await db.disconnect(group_id=group_id)
            return await m.reply('Gʀᴏᴜᴘ ᴅɪsᴄᴏɴɴᴇᴄᴛᴇᴅ')
        else:
            return await m.reply('Gʀᴏᴜᴘ ɪs ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ')
