# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64


async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(text="https://t.me/{Config.BOT_USERNAME}?start=JiC54_{str_to_b64(str(file_id))}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url="ttps://t.me/{Config.BOT_USERNAME}?start=JiC54_"+{_to_b64(str(file_id))})
                    ],
                    [
                        InlineKeyboardButton("🔄 close 🔄", callback_data='close_data')
                    ]
                ]
            ),
            
            disable_web_page_preview=True, quote=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await reply_forward(message, file_id)


async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id,
                                          reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url="https://t.me/{Config.BOT_USERNAME}?start=JiC54_{str_to_b64(str(file_id))}")
                    ],
                    [
                        InlineKeyboardButton("🔄 close 🔄", callback_data='close_data')
                    ]
                ]
            ),
            
            disable_web_page_preview=True, quote=True)
                                         )
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return media_forward(bot, user_id, file_id)


async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    await asyncio.sleep(2)
