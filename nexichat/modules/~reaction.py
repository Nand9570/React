from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat
import random

# Valid Telegram reaction emojis
valid_emojis = [
    "👍", "👎", "❤", "🔥", "🥰", "😂", "😢", "😡", "👏", 
    "🎉", "🤯", "🤩", "🤔", "🤗", "🤬", "💩", "💯", "😎"
]

@nexichat.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        # Randomly select a valid emoji
        random_emoji = random.choice(valid_emojis)
        await client.send_reaction(message.chat.id, message.id, [random_emoji])
    except Exception as e:
        print(f"Failed to react to message: {e}")
