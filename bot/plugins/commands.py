from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import TelegramBot
from bot.config import Telegram
from bot.static import *

@TelegramBot.on_message(
    filters.command('start')
    & (
        filters.private |
        filters.group
    )
)
async def start_command(_, msg: Message):
    return await msg.reply(
        text=WelcomeText % {'first_name': msg.from_user.first_name if msg.from_user else 'Anonymous'},
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ⇆', url=f'https://telegram.me/{Telegram.BOT_USERNAME}?startgroup=botstart')
                ],  [
        InlineKeyboardButton("• ᴜᴩᴅᴀᴛᴇꜱ •", url="https://t.me/sitaratoons"),
        InlineKeyboardButton("• ꜱᴜᴩᴩᴏʀᴛ •", url="https://t.me/+KjFf9hluSthkNjFl")
    ],  
                [
                    InlineKeyboardButton(text='⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ⇆', url=f'https://telegram.me/{Telegram.BOT_USERNAME}?startchannel=botstart')
                ]
            ]
        )
    )

@TelegramBot.on_message(
    filters.command('help')
    & (
        filters.private |
        filters.group
    )
)
async def send_emojis(_, msg: Message):
    return await msg.reply(
        text=Help,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='👨‍💻 ᴏᴡɴᴇʀ', url='https://telegram.me/CallOwnerBot'),
                    InlineKeyboardButton(text='💥 ʀᴇᴘᴏ', url='https://github.com/TechifyBots/Auto-Reaction-Bot')
                ]
            ]
        )
    )
