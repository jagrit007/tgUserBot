''' Insult module for uzerbot
-by ritik-gupta
'''

import random
from userbot import HELPER, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^.insult$")
async def insult(e):
    adjectives_start = ["salty", "fat", "fucking", "shitty", "stupid", "retarded", "self conscious", "tiny"]
    adjectives_mid = ["little", "vitamin D deficient", "idiotic", "incredibly stupid"]
    nouns = ["cunt", "pig", "pedophile", "beta male", "bottom", "retard", "ass licker", "cunt nugget",
                 "PENIS", "dickhead", "flute", "idiot", "motherfucker", "loner", "creep"]
    starts = ["You're a", "You", "Fuck off you", "Actually die you", "Listen up you",
                  "What the fuck is wrong with you, you"]
    ends = ["!!!!", "!", ""]
    start = random.choice(starts)
    adjective_start = random.choice(adjectives_start)
    adjective_mid = random.choice(adjectives_mid)
    noun = random.choice(nouns)
    end = random.choice(ends)
    insu = start + " " + adjective_start + " " + adjective_mid + (" " if adjective_mid else "") + noun + end
    await e.edit(insu)