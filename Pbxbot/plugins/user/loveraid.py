import random
from pyrogram import Client, filters
from pyrogram.enums import MessageEntityType as MET, ChatAction as CA
from pyrogram.types import Message
LRAID_STR = [
    "HAYEE MERI JAAN 🤩🤩",
    "MERI JAAN KITNI OSM HAI YAAR 😁🌹🌹😍😍😍",
    "I LOVE YOU MERI JAAN❤️❤️",
    "MERI JAAN I KISS YOU ❤️😋😊😘😘😘",
    "I MISS YOU JAAN 🥀🥀✨✨",
    "Mat muskurao itna ki Phoolo ko khabar lag jaye Ke wo kare taaref tumhari Aur tumhe unki najar lag jaye",
    "Chand se haseen hai chandni Chandni se haseen hai Raat Raat se haseen hai chand Aur chand se haseen hai aap",
    "You look so beautiful and pretty I feel lucky because you love me I love you now and I’ll always do Because I just can’t live without you",
    "Chand sa tera masoom chehra Tu haya ki ek murat hai Tujhe dekh ke kaliya bhi sharmaaye Tu itni khoobsurat hai",
    "कैसे करुं बयाँ मै खुबसुरती उसकी मेने तो उसे बिना देखे ही प्यार किया है।",
    "Mai tumhari sadagi ki kya misal du Is saare jaha me Be misaal ho tum",
    "LOVE YOU JAAN 😁😁🔥🔥😂",
    "I HUG YOU BABY 🤣🤣",
    "I LOVE YOU SO MUCH 🌹💫💖",
    "MADE BY DEV JAAN 😂😂",
    "нello 😍мerι jaan",
    "oye вaвy ѕυno na 😍",
    "ι love υ вaвe😘",
    "тυм нι нo🥺❤️",
    "आप ही के बिना हम क्यों बेचैन हैं",
    "आप ही क्यों मेरी जरूरत हैं",
    "वहम इतना हसीं नहीं होता",
    "वाकई आप खूबसूरत हैं",
    "ᴏyᴇ ʜᴏyᴇ ꜱᴀʀᴍᴀ ɢyɪ ᴋᴀᴀ ᴩʜᴏɴᴇ ᴋᴀᴛ ᴅɪ ᴍᴜᴍᴍy ᴀᴀ ɢyɪ ᴋyᴀ 🤣",
    "TU MAAN MERI JAAN TUJHE JANE NA DUNGA 🤣🤣✨",
    "TUJHE APNI BAHO ME SAJAKE 🤣🤣🤣",
    "EK UCHA LMBA KAD DUJA SONI HONI HAD TIJHA TERA RUP CHAM CHAM KR DANI TERE SIVHA DIL ME KOI UTRA THA NHI🤣🤣🤣🤣🌹🌹",
    "BS KHAFI HO GYI JHUT KI TARIF🤣🤣🤣",
    "HEY HA YOU....YOU ARE SO BEAUTIFUL ✨🌹 I LOVE YOU 🤣🥀🥀🥀✨✨🌹🌹",
    "MERI JAAN TUJHE NAZAR NA 🤣LGA JAYE KISI KI 🙄🆘",
    "KIN NA SONA TUJHE RAB NE BNAYA KI JI KRE DEKH THA RHU 😂😂🌹🌹❤️❤️😜🤣🤣",
    "LAL DUPATTA UD GYA HAYE MERI BEAUTY SE 🤣🤣😜😜",
    "BS BS HO GYI AB JHUTI TARIF JAAN 🤣🤣🤣",
    "#LOVE YOU JAAN",
    "I WANT YOU 👀BABY",
    "UMMMMM MAAA MERI JAAN 😍😘😘😘😘😘"
]

que = {}

# loveraid command to activate love raid
@on_message("loveraid", allow_stan=True)
async def loveraid_handler(client, message):
    global que
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        username = f"[{user.first_name}](tg://user?id={user.id})"
        await message.reply(f"Love Activating on {username}...")
        que[user.id] = []
        que[user.id].append(user.id)
        await client.send_message(
            chat_id=message.chat.id,
            text=random.choice(LRAID_STR),
            reply_to_message_id=message.reply_to_message.message_id
        )
    else:
        await message.reply("Please reply to a user to activate the love raid.")

# dloveraid command to deactivate love raid
@on_message("dlove", allow_stan=True)
async def dloveraid_handler(client, message):
    global que
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        username = f"[{user.first_name}](tg://user?id={user.id})"
        if user.id in que:
            que.pop(user.id)
            await message.reply(f"Love has been deactivated on {username}.")
        else:
            await message.reply(f"No love raid active on {username}.")
    else:
        await message.reply("Please reply to a user to deactivate the love raid.")
