# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //


from . import *
from .. import ATGK, ALIVE_NAME
from telethon import events, Button


ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "SPAMMER BOT"

@ATGK.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
    await event.reply("Sᴘᴀᴍᴍᴇʀ Bᴏᴛ Fᴏʀ f'{ALIVE_NAME}' Mᴀᴅᴇ Bʏ @CRiMiNaL786",
                    buttons=[
                        [Button.inline("Check Me",data="helpme")]
                    ])

@ATGK.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="I Aᴍ Sᴘᴀᴍᴍᴇʀ Bᴏᴛ!\nI Cᴀɴ Sᴘᴀᴍ Fᴏʀ Mʏ Mᴀsᴛᴇʀ.\n\nTʀʏ Mᴇ!! Rᴇϙᴜᴇsᴛ Cᴏᴅᴇ ɪɴ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ!"
    await event.edit(text,
                     buttons=[
                         [Button.url("ϲнαииєℓ", url="https://t.me/destroyxSupport")],
                         [Button.url("gяουρ", url="https://t.me/DesTRoYxOfficial")],
                         [Button.url("ɠเѵҽ α sԵαɾ ⭐", url="https://github.com/CRiMiNaL786")],
                         [Button.inline("ƒυϲκ", data="2")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="2"))
async def ex(event):
    text2="иοτнιиg нєяє ѕαя."
    await event.edit(text2,
                     buttons=[
                         [Button.inline("BacK", data="helpme")]
                     ])
