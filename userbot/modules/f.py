import random
import html
from userbot import HELPER, bot
from userbot.events import register

@register(outgoing=True, pattern=r"^.f")
async def fcmd(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text

        if message[-1] == 'p' and message[-2] == 'f':
            await e.edit("🤦‍♂")
        elif message[-1] == 'f':
            await e.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
    
        else:
            n= message[-1]
            out = ""
            for line in [5, 1, 1, 4, 1, 1, 1]:
                c = max(line, 1)
                out += (n * c) + "\n"
            await e.edit(html.escape(out))





