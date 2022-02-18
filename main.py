from pyrogram import Client, filters
from pyrogram.types import *
from gtts import gTTS

app = Client(session_name="Bot",
             api_hash='1b852557e771a37f4609749afeeeed78',
             api_id='427059',
             bot_token='5063247147:AAEbDZ72rJzmkxnc7uaUvLEF6HF3jdzXj4Y')


@app.on_message(filters.private)
async def GroupTextVoice(client, message):

    chat_id = message.chat.id
    username = message.from_user.username
    message_text = message.text

    message_text = str(message_text)
    text = message_text
    lang = 'en'

    obj = gTTS(text=text, lang=lang, slow=False)
    obj.save("obj.mp3")
    await app.send_audio(message.chat.id, "obj.mp3", caption="TextToVoice")

app.run()