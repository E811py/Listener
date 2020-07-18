from telethon import TelegramClient, events

lisens = [1131099953,821326656,828084817]
admin = 820586182

api_id = 1520270
api_hash = '82bd7b4562a5cd24d182bdc39b2d9352'
client = TelegramClient('thontes1', api_id, api_hash)

@client.on(events.NewMessage)
#async def handel(event):
#    print(event.chat.id)
async def handler(event):
    if event.sender_id in lisens:
        await client.forward_messages(-1001181274410, event.message)

    if event.sender_id == admin:
        if event.message.raw_text == "ping":
            await client.send_message(admin, 'im online')
#    chat = await event.get_chat()
#    sender = await event.get_sender()
#    chat_id = event.chat_id
#    sender_id = event.sender_id
#    print(f"getchat: {chat}\n-------------------\nsender: {sender}\n-----------------------\nchat_id: {chat_id}\n-----------------\nsender id: {sender_id}")

client.start()
client.run_until_disconnected()