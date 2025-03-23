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
        random_emoji = random.choice(emojis)  # Randomly select an emoji
        await message.react(random_emoji)
    except Exception as e:
        print(f"Failed to react to message: {e}")
