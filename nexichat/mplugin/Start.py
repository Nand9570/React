from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

@Client.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
        "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
        f"<b>    Hᴇʏ {message.from_user.first_name}! 👋</b>\n"
        "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n\n"
        "<b>⚡ Tʜɪs ɪs Yᴏᴜʀ Cʟᴏɴᴇᴅ Rᴇᴀᴄᴛɪᴏɴ Bᴏᴛ ⚡</b>\n\n"
        "<b>✅ I ʀᴇᴀᴄᴛ ᴛᴏ ᴀʟʟ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ 👍 ɪɴ</b>\n"
        "<b>ɢʀᴏᴜᴘs, ᴄʜᴀɴɴᴇʟs & ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs.</b>\n\n"
        "<b>➤ Aᴅᴅ ᴍᴇ ᴛᴏ ᴀɴʏ ɢʀᴏᴜᴘ ᴀɴᴅ sᴇᴇ ᴍᴇ ɪɴ ᴀᴄᴛɪᴏɴ!</b>\n\n"
        "<b>➤ Wᴀɴɴᴀ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ?</b>\n"
        "<b>ᴛʏᴘᴇ /clone ᴀɴᴅ ɢᴇᴛ ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ʀᴇᴀᴄᴛɪᴏɴ ʙᴏᴛ 😁</b>\n\n"
        "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>\n"
        '<b>       Mᴀᴅᴇ ʙʏ <a href="https://t.me/ShrutiBots">𝐒ʜʀᴜᴛɪ 𝐁ᴏᴛs</a></b>\n'
        '<b>       Pᴏᴡᴇʀᴇᴅ ʙʏ <a href="https://t.me/React_bbot">@React_bbot</a></b>\n'
        "<b>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</b>",
        disable_web_page_preview=True
    )
