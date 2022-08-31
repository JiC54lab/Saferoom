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
            f"**Here is Sharable Link of this file:**\n"
            f"https://t.me/{Config.BOT_USERNAME}?start=AbirHasan2005_{str_to_b64(str(file_id))}\n\n"
            f"__To Retrive the Stored File, just open the link!__",
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
                                InlineKeyboardButton("♻️Retrive File♻️", url=f"https://t.me/{Config.BOT_USERNAME}?start=AbirHasan2005_{str_to_b64(str(file_id))}")
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


async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    await bot.send_message('Decrypting file...\n**ETA** ```1m13s```')
 
        rju1 = await f"Decrypting file...\n**ETA** ```1m13s```".edit('Decrypting file...\n**ETA** ```41s```')

        rju2 = await rju1.edit('Decrypting file...\n**ETA** ```19s```')

        rju3 = await rju2.edit('Decrypting file...\n**ETA** ```4s```')
        rju4 = await rju3.edit('Decryption Complete! Uploading starts...⏳')
        rju5 = await rju4.edit('Decryption Complete! Uploading starts...⌛️')
        rju6 = await rju5.edit('Uploading\n▣▣▢▢▢▢ 27%')
        rju7 = await rju6.edit('Uploading\n▣▣▣▢▢▢ 50%')
        rju8 = await rju7.edit('Uploading\n▣▣▣▣▢▢ 66%')
        rju9 = await rju8.edit('Uploading\n▣▣▣▣▣▢ 83%')
        rju10 = await rju9.edit('Uploading\n▣▣▣▣▣▣ 97%')
        await rju10.delete()
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    await asyncio.sleep(2)
