import random
import html
from userbot import HELPER, bot
from userbot.events import register

@register(outgoing=True, pattern=r"^.f")
async def fcmd(message):
    n = message.text[-1]
    if (message.text[-1] == 'f' or message.text[-1] == ' ') and message.text[0]=='.':
        await message.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
    
    elif message.text[0]=='.':
        out = ""
        for line in [5, 1, 1, 4, 1, 1, 1]:
            c = max(line, 1)
            out += (n * c) + "\n"
        await message.edit(html.escape(out))





