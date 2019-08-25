from pyrogram import Client, Filters

import requests

from bs4 import BeautifulSoup

import traceback

API_URL = "http://sci-hub.tw/"

users = {}

@Client.on_message(Filters.private & Filters.incoming)
def _core(c, m):

    if(users.get(m.chat.id)):
        return
    
    users[m.chat.id] = True
    
    m.reply_chat_action("typing")
    
    MSG = "Processing....."
    
    snt = m.reply_text(text = MSG, disable_notification = True, quote = True)
    
    session = requests.Session()
    
    req_url = API_URL+m.text
    
    headers = {'User-Agent':"Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        'Accept-Language':"en-US,en;q=0.9",
        'Proxy-Authorization':"Basic VVZQTnYyLTU5NWIzYjc5Mzk2MTc1YmEzNmExNjMxNWFiNmI4OTM5NTA4MmUxYzdhNDA1MTI0MGE5ZTA1NGRhMTU3NWJjOTUmYzgwdjBAZW1haWx0ZXguY29tOjJjZTY3NTA1Mjg0NjZlNDczNzY0ZTU1ZmRiNDgzODFhZTNkZmUyOWI5MDZiMmVlYzA3YTljNjc3ODFlOGM5OTI="
    }           

    try:
        
        s = session.get(API_URL, headers=headers)
        
        r = session.get(req_url, headers=headers)
        
        soup = BeautifulSoup(r.text, "html.parser")
        
        article = soup.find("div", id="article")
        
        if(not article):
            
            print('Error!')
            
            snt.edit_text(text = "The document you tried to unlock might not be available or the link/DOI you provided is invalid.")
            
            users.pop(m.chat.id)
            
            return
        
        file_url = article.iframe['src'].split('#')[0]
        
        if(not file_url.startswith('http')):
            
            file_url = 'http:'+file_url
        
        snt.edit_text(text = f"Unlocked document URL.\n\n{file_url}")
        
        users.pop(m.chat.id)
        
        return
    
    except:
        
        traceback.print_exc()
        
        snt.edit_text(text = "The document you tried to unlock might not be available or the link/DOI you provided is invalid.")
        
        users.pop(m.chat.id)
        
        return
    
