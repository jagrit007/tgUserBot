import random
import html
from userbot import HELPER, bot
from userbot.events import register

@register(outgoing=True, pattern=r"^.f")
async def fcmd(message):
    n = len(message)
    args = message[4]
    if n <= 3:
        await message.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
    
    if n > 3:
        out = ""
        for line in [5, 1, 1, 4, 1, 1, 1]:
            c = max(round(line / (n-3)), 1)
            out += (args * c) + "\n"
        await message.edit("<code>" + html.escape(out) + "</code>")





