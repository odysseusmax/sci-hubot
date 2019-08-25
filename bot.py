from pyrogram import Client
import os


plugins = dict(root="plugins",
    include=[
        "start",
        "help",
        "core"
    ]
)

API_ID = int(os.environ['api_id'])
API_HASH = os.environ['api_hash']
BOT_TOKEN = os.environ['session_name']

Client("sci_hubot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH,
    workers=50,
    plugins=plugins
).run()
