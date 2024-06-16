import discord
from discord.ext import commands

# import os
# from dotenv import load_dotenv

from private.config import token

intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False

bot = discord.Client(intents=intents)
#bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has arrived!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'rand' in message.content.lower():
        await message.channel.send(f'{bot.user.name} is at your service! Open me up with a command and I will reveal it all to you!')


bot.run(token)