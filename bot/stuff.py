0#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nThis is A Compressor Bot Which Can Compress reduce size of Videos.\nReduce Size of Videos With Negligible Quality Change🥰🥰\nU For further information contact @Anshu888o Do not mess with my private chat everytime I am busy guy😔.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("MOVIES GROUP", url="https://t.me/GorgeousAndGloreous"),
                Button.url("DEVELOPER", url="t.me/Anshu888o"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "♡☆ A Quality Compress Bot**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Nothing else🤫\n+LOVE U MUMMY\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience and Send videos One By One After Completing.\nDont Spam Bot or mess with me.\n\nJust Forward Video To Get Options no no sorry i forget that BOT is automatic😜"
    )


async def ihelp(event):
    await event.edit(
        "♡☆ A Quality Compress Bot**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Nothing else🤫\n+LOVE U MUMMY\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience and Send videos One By One After Completing.\nDont Spam Bot or mess with me.\n\nJust Forward Video To Get Options no no sorry i forget that BOT is automatic😜",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\nThis is A Compressor Bot Which Can Compress reduce size of Videos.\nReduce Size of Videos With Negligible Quality Change🥰🥰\nU For further information contact @Anshu888o Do not mess with my private chat everytime I am busy guy😔.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("MOVIES BOT", url="https://t.me/GorgeousAndGloreous"),
                Button.url("DEVELOPER", url="t.me/Anshu888o"),
            ],
        ],
    )
