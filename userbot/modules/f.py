import random
from userbot import HELPER, bot
from userbot.events import register

@register(outgoing=True, pattern=r"^.f")
async def fcmd(message):
    await message.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")





