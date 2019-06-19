from userbot import bot
from telethon import events
import asyncio
from datetime import datetime
from telethon.tl.types import User, Chat, Channel


@bot.on(events.NewMessage(pattern=r"\.stats", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    dialogs = await bot.get_dialogs(
        limit=None,
        ignore_migrated=True
    )
    for d in dialogs:
        currrent_entity = d.entity
        if type(currrent_entity) is User:
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif type(currrent_entity) is Chat:
            g += 1
        elif type(currrent_entity) is Channel:
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit("""`Your Stats Obtained in {} seconds`
`You have {} Private Messages`
`You are in {} Groups`
`You are in {} Super Groups`
`You Are in {} Channels`
`And finally Bots = {}`""".format(ms, u, g, c, bc, b))

