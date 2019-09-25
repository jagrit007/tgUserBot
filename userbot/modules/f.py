import random
import html
from userbot import HELPER, bot
from userbot.events import register

@register(outgoing=True, pattern=r"^.f")
async def fcmd(message):
    n = message.text[-1]
    if n==' ' or n=='f':
        await message.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
    
    else:
        out = ""
        for line in [5, 1, 1, 4, 1, 1, 1]:
            c = max(line, 1)
            out += (n * c) + "\n"
        await message.edit("<code>" + html.escape(out) + "</code>")





