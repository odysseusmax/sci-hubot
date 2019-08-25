from pyrogram import Client, Filters

@Client.on_message(Filters.private & Filters.incoming & Filters.command(['start']))
def _start(c, m):

    m.reply_chat_action("typing")
    
    MSG = f"Hi {m.from_user.first_name}.\n\nI'm Sci-Hub bot. Bot which unlocks and provide public access to research papers. /help to know more."
    
    m.reply_text(text = MSG, disable_notification = True, quote = True)
