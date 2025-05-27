import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} giriş yaptı!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!selam'):
        await message.channel.send(f'Merhaba, {message.author.name}!')

    if message.content.startswith('!yardım'):
        await message.channel.send("Komutlar:\n`!selam` - Selamlaşır\n`!yardım` - Yardım menüsünü gösterir")

client.run(TOKEN)
