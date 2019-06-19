# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio
from asyncio import wait

from userbot import LOGGER_GROUP, LOGGER, HELPER
from userbot.events import register
from userbot import BRAIN_CHECKER

@register(outgoing=True, pattern="^.spam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if e.chat_id in BRAIN_CHECKER:
            await e.edit("`Not supposed to spam in Sudo Chat!`")
        else:
            message = e.text
            counter = int(message[6:8])
            spam_message = str(e.text[8:])
            await asyncio.wait([e.respond(spam_message) for i in range(counter)])
            await e.delete()
            if LOGGER:
                await e.client.send_message(
                    LOGGER_GROUP,
                    "#SPAM \n\n"
                    "Spam was executed successfully"
                    )

@register(outgoing=True, pattern="^.bigspam")
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if e.chat_id in BRAIN_CHECKER:
            await e.edit("`Not supposed to spam in Sudo chat!`")
        else:
            message = e.text
            counter = int(message[9:13])
            spam_message = str(e.text[13:])
            for i in range(1, counter):
                await e.respond(spam_message)
            await e.delete()
            if LOGGER:
                await e.client.send_message(
                    LOGGER_GROUP,
                    "#BIGSPAM \n\n"
                    "Bigspam was executed successfully"
                    )


@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if e.chat_id in BRAIN_CHECKER:
            await e.edit("`Not supposed to spam in Sudo chat!`")
        else:
            message = e.text
            text = message.split()
            counter = int(text[1])
            link = str(text[2])
            for i in range(1, counter):
                await e.client.send_file(e.chat_id, link)
            await e.delete()
            if LOGGER:
                await e.client.send_message(
                    LOGGER_GROUP,
                    "#PICSPAM \n\n"
                    "PicSpam was executed successfully"
                    )

#end of file
