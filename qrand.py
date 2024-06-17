import discord
from discord.ext import commands
import json
import random

from private.config import token

intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False

bot = discord.Client(intents=intents)
#bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has arrived!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await message.channel.send('Call me Rand! Call me names!')

    if 'rand' in message.content.lower():
        await message.channel.send(f'If you call this {bot.user.name} bot names like:\n!absurd\n!begairat\nit will return a quote to prove you right!')

    if 'absurd' in message.content.lower():
        f = open('absurdity.json')
        data = json.load(f)
        key = random.choice(list(data))
        output1 = key['description']
        output2 = key['url']
        await message.channel.send(output1)
        await message.channel.send(output2)

    if 'begairat' in message.content.lower():
        f = open('nikah.json')
        data = json.load(f)
        key = random.choice(list(data))
        output1 = key['description']
        output2 = key['url']
        await message.channel.send(output1)
        await message.channel.send(output2)

bot.run(token)
