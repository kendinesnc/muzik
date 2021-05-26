from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hoşgeldin **Ben Netd Music 📀** Grubunuzda Şarkı Arayabilirim Stabil Çalışmam İçin Bana Herhangi Bir Yetki Verin 👁 
 Kullanım Şekli : **/e < şarkı adı>** Örnek : /e suspus
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sahibi 💬", url="https://t.me/Azerbesk"
                    ),
                    InlineKeyboardButton(
                        "Kanal 📣", url="https://t.me/KaybedenlerOrkestrasi"
                        )
                ]
            ]
        )
    )
