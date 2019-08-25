from pyrogram import Client, Filters

@Client.on_message(Filters.private & Filters.incoming & Filters.command(['help']))
def _help(c, m):

    m.reply_chat_action("typing")
    
    MSG = f"Hi {m.from_user.first_name}.\n\nSend me any valid IEEE Document URL or valid DOI. If available, I'll reply the unlocked URL of the document."
    
    m.reply_text(text = MSG, disable_notification = True, quote = True)
