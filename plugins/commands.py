from datetime import datetime
from configs import Config
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TeamTeleRoid.database import db


@Client.on_message(filters.command("help") & filters.private)
async def help_handler(_, event: Message):
    await event.reply_text(Config.ABOUT_HELP_TEXT.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [
            InlineKeyboardButton('➕ Add Me To Your Groups ➕', url=f'http://t.me/{Config.BOT_USERNAME}?startgroup=true')
            ],

             [InlineKeyboardButton("About", callback_data="About_msg"),
             InlineKeyboardButton("Help", callback_data="Help_msg")
             ]
        ])
    )                        

@Client.on_message(filters.command("Watch") & filters.private)
async def watch_handler(_, event: Message):
    await event.reply_text(Config.ABOUT_WATCH_TEXT.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [
            InlineKeyboardButton("Click Me For Tutorials", callback_data="Watch_msg")
             ]
        ])
    ) 

@Client.on_message(filters.command("Mdisk") & filters.private)
async def mdisk_handler(_, event: Message):
    await event.reply_text(Config.ABOUT_MDISK_TEXT.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [
            InlineKeyboardButton('➕ Add Me To Your Groups ➕', url=f'http://t.me/{Config.BOT_USERNAME}?startgroup=true')
            ],

             [InlineKeyboardButton("TeraBox", callback_data="Terabox_msg"),
             InlineKeyboardButton('Watch Video', url='https://t.me/movies_villa_backup')
             ]
        ])
    )

@Client.on_message(filters.command("Terabox") & filters.private)
async def terabox_handler(_, event: Message):
    await event.reply_text(Config.ABOUT_TERABOX_TEXT.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [
            InlineKeyboardButton('➕ Add Me To Your Groups ➕', url=f'http://t.me/{Config.BOT_USERNAME}?startgroup=true')
            ],

             [InlineKeyboardButton("Mdisk", callback_data="Mdisk_msg"),
             InlineKeyboardButton('Watch Photo', url='https://telegra.ph/file/abdc2f0e2d59f6bb67fa5.jpg')
             ]
        ])
    )

@Client.on_message(filters.command('leave') & filters.private &  filters.chat(Config.BOT_OWNER))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('Support', url=f'https://t.me/movies_villa_backup')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>Hᴇʟʟᴏ Fʀɪᴇɴᴅs, \nMʏ ᴀᴅᴍɪɴ ʜᴀs Gɪᴠᴇɴ Mᴇ Cᴏᴍᴍᴀɴᴅ Tᴏ Lᴇᴀᴠᴇ Yᴏᴜʀ Gʀᴏᴜᴘ,Sᴏ I Hᴀᴠᴇ Tᴏ Gᴏ Pʟᴇᴀsᴇ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ Fᴏʀ Aɴʏ Hᴇʟᴘ.</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
        await message.reply(f"left the chat `{chat}`")
    except Exception as e:
        await message.reply(f'Error - {e}')

@Client.on_message(filters.command("usend") & filters.private &  filters.chat(Config.BOT_OWNER))
async def send_msg(bot, message):
    if message.reply_to_message:
        target_id = message.text
        command = ["/usend"]
        for cmd in command:
            if cmd in target_id:
                target_id = target_id.replace(cmd, "")
        success = False
        try:
            user = await bot.get_users(int(target_id))
            await message.reply_to_message.copy(int(user.id))
            success = True
        except Exception as e:
            await message.reply_text(f"<b>Eʀʀᴏʀ :- <code>{e}</code></b>")
        if success:
            await message.reply_text(f"<b>Yᴏᴜʀ Mᴇssᴀɢᴇ Hᴀs Bᴇᴇɴ Sᴜᴄᴄᴇssғᴜʟʟʏ Sᴇɴᴛ Tᴏ {user.mention}.</b>")
        else:
            await message.reply_text("<b>Aɴ Eʀʀᴏʀ Oᴄᴄᴜʀᴇᴅ !</b>")
    else:
        await message.reply_text("<b>Cᴏᴍᴍᴀɴᴅ Iɴᴄᴏᴍᴘʟᴇᴛᴇ...</b>")

@Client.on_message(filters.command("gsend") & filters.private &  filters.chat(Config.BOT_OWNER))
async def send_chatmsg(bot, message):
    if message.reply_to_message:
        target_id = message.text
        command = ["/gsend"]
        for cmd in command:
            if cmd in target_id:
                target_id = target_id.replace(cmd, "")
        success = False
        try:
            chat = await bot.get_chat(int(target_id))
            await message.reply_to_message.copy(int(chat.id))
            success = True
        except Exception as e:
            await message.reply_text(f"<b>Eʀʀᴏʀ :- <code>{e}</code></b>")
        if success:
            await message.reply_text(f"<b>Yᴏᴜʀ Mᴇssᴀɢᴇ Hᴀs Bᴇᴇɴ Sᴜᴄᴄᴇssғᴜʟʟʏ Sᴇɴᴛ Tᴏ {chat.id}.</b>")
        else:
            await message.reply_text("<b>Aɴ Eʀʀᴏʀ Oᴄᴄᴜʀᴇᴅ !</b>")
    else:
        await message.reply_text("<b>Cᴏᴍᴍᴀɴᴅ Iɴᴄᴏᴍᴘʟᴇᴛᴇ...</b>")


@Client.on_message(filters.command("Owner") & filters.group)
async def report_user(bot, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        admins = await bot.get_chat_members(chat_id=chat_id, filter="administrators")
        success = True
        report = f"𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})" + "\n"
        report += f"𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {message.reply_to_message.link}"
        for admin in admins:
            try:
                reported_post = await message.reply_to_message.forward(Config.BOT_OWNER)
                await reported_post.reply_text(
                    text=report,
                    chat_id=admin.user.id,
                    disable_web_page_preview=True
                )
                success = True
            except:
                pass
        if success:
            await message.reply_text("Hᴇʏ {user.mention} Yᴏᴜʀ Mᴇssᴀɢᴇ Hᴀs Bᴇᴇɴ Sᴜᴄᴄᴇssғᴜʟʟʏ Sᴇɴᴛ Tᴏ Bᴏᴛ Oᴡɴᴇʀ!")

@Client.on_message(filters.command('Glink') & filters.private &  filters.chat(Config.BOT_OWNER))
async def gen_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('Gɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀᴛ ɪᴅ')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Gɪᴠᴇ Mᴇ A Vᴀʟɪᴅ Cʜᴀᴛ ID')
    try:
        link = await bot.create_chat_invite_link(chat)
        return await message.reply("Iɴᴠɪᴛᴇ Lɪɴᴋ Gᴇɴᴇʀᴀᴛɪᴏɴ Fᴀɪʟᴇᴅ, Iᴀᴍ Nᴏᴛ Hᴀᴠɪɴɢ Sᴜғғɪᴄɪᴇɴᴛ Rɪɢʜᴛs")
    except Exception as e:
        return await message.reply(f'Error {e}')
    await message.reply(f'Here is your Invite Link {link.invite_link}')

@Client.on_message(filters.command("users") & filters.private &  filters.chat(Config.BOT_OWNER))
async def total_users(_, event: Message):
    total_users = await db.total_users_count()
    msg = f"""
    Users: {total_users} users

    """
    await event.reply_text(msg)

@Client.on_message( filters.command("start") & filters.private)
async def start_handler(_,event: Message):
    await event.reply_photo(
        photo=Config.START_PHOTO,
        caption=Config.START_MSG.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [
            InlineKeyboardButton('➕ Add Me To Your Groups ➕', url=f'http://t.me/{Config.BOT_USERNAME}?startgroup=true')
            ],

             [InlineKeyboardButton("About", callback_data="About_msg"),
             InlineKeyboardButton("Help", callback_data="Help_msg")
             ]
        ])
    )

VERIFY = {}
@Client.on_message(filters.command("License") & filters.group)
async def request_handler(c,m: Message):
    global VERIFY
    chat_id = m.chat.id
    user_id = m.from_user.id if m.from_user else None


    if VERIFY.get(str(chat_id)) == None: # Make Admin's ID List
        admin_list = []
        async for x in c.iter_chat_members(chat_id=chat_id, filter="administrators"):
            admin_id = x.user.id 
            admin_list.append(admin_id)
        admin_list.append(None)
        VERIFY[str(chat_id)] = admin_list

    if not user_id in VERIFY.get(str(chat_id)): # Checks if user is admin of the chat
        return

    group_id = m.chat.id
    group_info = await db.get_group(group_id)

    if not group_info["has_access"] or not await db.is_group_verified(group_id):
        REPLY_MARKUP = InlineKeyboardMarkup([
            [
                InlineKeyboardButton('Rᴇǫᴜᴇsᴛ Aᴄᴄᴇss', callback_data=f'request_access#{m.chat.id}#{m.from_user.id}'),
            ],

        ])

        return await m.reply_text(f"Yᴏᴜʀ ɢʀᴏᴜᴘ ᴍᴀʏ ɴᴏᴛ ʜᴀᴠᴇ ᴀᴄᴄᴇss ᴛᴏ ᴀᴅᴅ ʏᴏᴜʀ ᴏᴡɴ Dᴀᴛᴀʙᴀsᴇ Cʜᴀɴɴᴇʟ ᴏʀ ᴍᴀʏ ʜᴀᴠᴇ ᴇxᴘɪʀᴇᴅ. Pʟᴇᴀsᴇ Gᴇᴛ Lɪᴄᴇɴsᴇ Fʀᴏᴍ ᴛʜᴇ ᴀᴅᴍɪɴ" ,reply_markup=REPLY_MARKUP ,disable_web_page_preview=True)

    else:
        return await m.reply_text("Yᴏᴜʀ ɢʀᴏᴜᴘ ᴀʟʀᴇᴀᴅʏ ʜᴀᴠᴇ ᴀᴄᴄᴇss ᴛᴏ /database")


@Client.on_message(filters.command("Database") & filters.group)
async def addb_handler(c, m: Message):
    global VERIFY
    chat_id = m.chat.id
    user_id = m.from_user.id if m.from_user else None


    if VERIFY.get(str(chat_id)) == None: # Make Admin's ID List
        admin_list = []
        async for x in c.iter_chat_members(chat_id=chat_id, filter="administrators"):
            admin_id = x.user.id 
            admin_list.append(admin_id)
        admin_list.append(None)
        VERIFY[str(chat_id)] = admin_list

    if not user_id in VERIFY.get(str(chat_id)): # Checks if user is admin of the chat
        return

    group_id = m.chat.id
    group_info = await db.get_group(str(group_id))

    if group_info["has_access"] and await db.is_group_verified(group_id):
        if len(m.command) == 2:
            db_channel = m.command[1]


            try:
                invite_link =  await c.create_chat_invite_link(int(db_channel))
            except Exception as e:
                return await m.reply_text("Mᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ʏᴏᴜ ʜᴀᴠᴇ ᴍᴀᴅᴇ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ɪɴ ᴜʀ ᴄʜᴀɴɴᴇʟ "+str(db_channel))
                

            REPLY_MARKUP = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('Allow DB Channel', callback_data=f'dbgive_access#{group_id}#{m.from_user.id}#{db_channel}'),
            InlineKeyboardButton('Deny', callback_data=f'dbdeny_access#{m.from_user.id}#{db_channel}'),
        ],
        [
            
            InlineKeyboardButton('Close', callback_data=f'delete'),
        ],

    ])      

            await c.send_message(Config.LOG_CHANNEL,  f"Jᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇɴ ᴀʟʟʟᴏᴡ.\n\n#NewDBChannel\n\nDB Cʜɴʟ Iɴᴠɪᴛᴇ Lɪɴᴋ: {invite_link.invite_link}\nGroup:`{group_id}`\n\nNᴏᴛᴇ: Tʜɪs ɢʀᴏᴜᴘ ʜᴀs ʙᴇᴇɴ ᴀʟʀᴇᴀᴅʏ ʜᴀs ᴀᴄᴄᴇss", reply_markup=REPLY_MARKUP)
            return await m.reply_text("Dᴀᴛᴀʙᴀsᴇ Cʜᴀɴɴᴇʟ Rᴇǫᴜᴇsᴛ Sᴇɴᴛ sᴜᴄᴄᴇssғᴜʟʟʏ. Wᴀɪᴛ ғᴏʀ ᴛʜᴇ ᴀᴅᴍɪɴ ᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ᴛʜᴇ Yᴏᴜʀ Dᴀᴛᴀʙᴀsᴇ ᴄʜᴀɴɴᴇʟ. Yᴏᴜ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪғɪᴇᴅ Iɴ Yᴏᴜʀ Pʀɪᴠᴀᴛᴇʟʏ Fʀᴏᴍ Tʜᴇ Bᴏᴛ", )
        else:
            return await m.reply_text("Mᴀᴋᴇ ᴛʜᴇ ʙᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ /database -100xxx")
    else:
        return await m.reply_text("Yᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴏᴇs ɴᴏᴛ ʜᴀᴠᴇ ᴀᴄᴄᴇss ᴛᴏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ. Pʟᴇᴀsᴇ Gᴇᴛ /License Aɢᴀɪɴ Fᴏʀ ᴀᴄᴄᴇss")
