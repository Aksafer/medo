
import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram import filters, Client
from MatrixMusic import app
from config import OWNER_ID

@app.on_message(filters.command(["بوت","البوت"], prefixes=""))
async def Italymusic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    italy = message.from_user.mention
    button = InlineKeyboardButton("اضف البوت الي مجموعتك⚡", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 6905129434:
             rank = "مـبـرمـج الـسورس ,💕"
        elif user_id == OWNER_ID:
             rank = "مـطـور الـبـوت يـا مـعـلـم ,💕"
        elif member.status == 'creator':
             rank = "مـالـك الـجـروب يـا مـعـلـم ,💕"
        elif member.status == 'administrator':
             rank = "مـشـرف الـجـرو يـا مـعـلـم ,💕"
        else:
             rank = "بـطـل لـعـب يـلا انـت مـش مـشـرف ,🔫"
    except Exception as e:
        print(e)
        rank = "مـلـوش مـلـه و بـيـتـكـلـم ,🔫"
    async for photo in client.get_chat_photos("me", limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""نـعـم يـمـعـلـم⇦ {italy}  عـوز ايـه\n\n انـا بـوت اسـمـي ⇦ {bot_name} \n\nرتـبـتـك هـيـا ⇦{rank}""", reply_markup=keyboard)


