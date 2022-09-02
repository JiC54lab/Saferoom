# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64


async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"**<u>Here's sharable link of this File:**</u>\n"
            f'📋: "```https://t.me/{Config.BOT_USERNAME}?start=JiC54_{str_to_b64(str(file_id))}```"\n\n'
            f"Just tap to copy link or press **♻️Retrive File♻️** To Retrive the Stored File",
            disable_web_page_preview=True, quote=True)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await reply_forward(message, file_id)


async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id,
                                          reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Retrive File♻️", url=f"https://t.me/{Config.BOT_USERNAME}?start=JiC54_{str_to_b64(str(file_id))}"),
                                InlineKeyboardButton("Share Link↗️", url=f"https://t.me/share/url?url=https://t.me/{Config.BOT_USERNAME}?start=JiC54_{str_to_b64(str(file_id))}") 
                            ]
                        ]
                    )
                                          )
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)


async def send_media_and_reply(bot: Client, editable: Message, user_id: int, file_id: int):
    halla = await editable.reply(
            "**decrypting**")
    halla1 = await halla.edit("0%")
    halla2 = await halla1.edit("50%")
    halla3 = await halla2.edit("80%")
    await halla3.edit("100%")
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    await asyncio.sleep(2)
