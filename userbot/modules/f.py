import random
import html
from userbot import HELPER, bot
from userbot.events import register

@register(outgoing=True, pattern=r"^.f")
async def fcmd(e):
    message = e.text
    if message == ".fp" and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")

    elif message == '.f' and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
    
    elif message.text[0]=='.' and e.text[0] not in ("/", "#", "@", "!"):
        n= message[-1]
        out = ""
        for line in [5, 1, 1, 4, 1, 1, 1]:
            c = max(line, 1)
            out += (n * c) + "\n"
        await message.edit(html.escape(out))





