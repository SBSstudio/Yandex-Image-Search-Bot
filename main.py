# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Yandex-Image-Search-Bot/blob/main/LICENSE

import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import *


Bot = Client(
    "Yandex-Image-Search-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

API = "https://apibu.herokuapp.com/api/y-images?query="


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=f"Hello {update.from_user.mention}, \n\nI am a yandex image search bot. You can use me in inline. Send name you want to Download. \n\n@Yandeximagesearchbot|@SBS_Studio",
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.text)
async def filter_text(bot, update):
    await update.reply_text(
        text=f"Click the button below for searching your query.\n\nQuery: `{update.text}`",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Search Now 🔎", switch_inline_query_current_chat=update.text)],
                [InlineKeyboardButton(text="Go Inline 🛒", switch_inline_query=update.text)]
                [InlineKeyboardButton(text="Update Channel 🗣", url="https://t.me/SBS_Studio")]
            ]
        ),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_inline_query()
async def search(bot, update):
    results = requests.get(API + requote_uri(update.query)).json()["result"][50:]
    answers = []
    for result in results:
        answers.append(
            InlineQueryResultPhoto(
                title=update.query,
                description=result,
                caption="@Yandeximagesearchbot|@SBS_Studio",
                photo_url=result
            )
        )
    await update.answer(answers)


Bot.run()
