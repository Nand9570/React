from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

@nexichat.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
        "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
        f"<b>    Hᴇʟʟᴏ {message.from_user.first_name}! 👋</b>\n"
        "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n\n"
        "<b>⚡ Wᴇʟᴄᴏᴍᴇ ᴛᴏ @React_bbot ⚡</b>\n\n"
        "<b>I'ᴍ ᴀ Rᴇᴀᴄᴛɪᴏɴ Bᴏᴛ ᴛʜᴀᴛ ʀᴇᴀᴄᴛs ᴛᴏ ᴀʟʟ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ</b>\n"
        "<b>ᴀ ᴛʀᴇɴᴅʏ 👍 ᴇᴍᴏᴊɪ ɪɴ Gʀᴏᴜᴘs, Cʜᴀɴɴᴇʟs & Pᴍs!</b>\n\n"
        "<b>➤ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ Gʀᴏᴜᴘ ᴀɴᴅ ᴡᴀᴛᴄʜ ᴛʜᴇ ᴍᴀɢɪᴄ!</b>\n\n"
        "<b>➤ Cʀᴇᴀᴛᴇ Yᴏᴜʀ Oᴡɴ Bᴏᴛ?</b>\n"
        "<b>ᴛʏᴘᴇ: /clone ᴀɴᴅ ɢᴇᴛ ʏᴏᴜʀ ᴏᴡɴ ᴠᴇʀsɪᴏɴ 😁</b>\n\n"
        "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
        '<b>       Mᴀᴅᴇ ʙʏ <a href="https://t.me/ShrutiBots">𝐒ʜʀᴜᴛɪ 𝐁ᴏᴛs</a> Fᴏʀ Fᴜɴ</b>\n'
        "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>"
    )
