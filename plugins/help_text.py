#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# the secret configuration specific things
from sample_config import Config


# the Strings used for this "thing"
from translation import Translation

import pyrogram
from telethon.sync import TelegramClient,events,Button
from telethon import custom, events, Button, functions
import telethon

from telethon.tl.types import (
    Channel,
    Chat,
    User
)

from sample_config import Config

logging.basicConfig(level=logging.WARNING)
api_id = Config.APP_ID
api_hash = Config.API_HASH


bott = TelegramClient(None, api_id, api_hash)
BOT_TOKEN = Config.TG_BOT_TOKEN
client = bott.start(bot_token=BOT_TOKEN)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    # await bot.ReplyKeyboardMarkup(
    #     chat_id=update.chat.id,
    #     text=Translation.HELP_USER,
    #     parse_mode="html",
    #     disable_web_page_preview=True,
    #     reply_to_message_id=update.message_id,
    #
    # )
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
    keyboard = [[InlineKeyboardButton(text="HeavenBots", url="t.me/heaven_CHATS")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.reply_text('Join Our Telegram Group For Support',
                                      reply_markup=reply_markup)


def first(bot,update):
        query = update.callback_query
        #reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=query.message.chat_id,
                         text='hi')
@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    TRChatBase(update.from_user.id, update.text, "/start")
    keyboard = [    [
        InlineKeyboardButton("OUR GROUP",  url="t.me/heaven_CHATS"),
        
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(name=update.chat.first_name),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,

        reply_markup=reply_markup,
    )



@pyrogram.Client.on_message(pyrogram.filters.command(["plan"]))
async def plan(bot, update):
    TRChatBase(update.from_user.id, update.text, "/plan")
    textt = """Current plan details
--------
Telegram ID: <code>@{price}</code>
Plan name: HEAVEN USER
Expires on: WOW THERES NO EXPIRY DATE"""

    await bot.send_message(
        chat_id=update.chat.id,
        text=textt.format(price= update.chat.username),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
