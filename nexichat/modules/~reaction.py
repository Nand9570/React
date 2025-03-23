from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat
import random

# Expanded emoji list
emojis = [
    "❤️", "🔥", "😂", "😍", "😎", "💘", "😜", "👍", "🥰", "😇", "🤩", "🤔", "💥", "💫", "💖", "👀",
    "😅", "🤣", "😋", "🤗", "💯", "✨", "👑", "💓", "😏", "🙃", "💥", "🤡", "😌", "💢", "😻", "👾",
    "🙌", "🤝", "😈", "🎉", "👋", "😶‍🌫️", "🫶", "🥳", "🤑", "😴", "👻", "💎", "🌈", "💫", "⚡"
]

@nexichat.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        random_emoji = random.choice(emojis)  # Select random emoji
        await client.send_reaction(message.chat.id, message.id, [random_emoji])  # Emoji in list format
    except Exception as e:
        print(f"Failed to react to message: {e}")
