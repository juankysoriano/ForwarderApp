from telethon import TelegramClient
from telethon.utils import get_display_name
import asyncio

async def retrieve_messages():
    client = TelegramClient('session_id', api_id=7713896, api_hash='7ffeb35617513a21e147e1cd75106734')
    await client.start()
    dialogs = await client.get_dialogs(30)
    for i in range(len(dialogs)):
        print(dialogs[i])
        print("---")
    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(retrieve_messages())
