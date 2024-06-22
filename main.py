import discord
from discord.ext import commands
import json
import random


import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has arrived!')
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await message.channel.send('Call me Random names!')

    if 'rand' in message.content.lower():
        await message.channel.send(f'If you call this {bot.user.name} names like:\nSTUPID\nDANGARR\nZALIM\nit will return a quote to prove you right!\nMore insults coming soon...')

    if 'stupid' in message.content.lower():
        f = open('absurdity.json')
        data = json.load(f)
        key = random.choice(list(data))
        output1 = key['description']
        output2 = key['url']
        await message.channel.send(output1)
        await message.channel.send(output2)

    if 'dang' in message.content.lower():
        f = open('nikah.json')
        data = json.load(f)
        key = random.choice(list(data))
        output1 = key['description']
        output2 = key['url']
        await message.channel.send(output1)
        await message.channel.send(output2)

    if 'zalim' in message.content.lower():
        f = open('cruelty.json')
        data = json.load()
        key = random.choice(list(data))
        output1 = key['description']
        output2 = key['url']
        await message.channel.send(output1)
        await message.channel.send(output2)

bot.run(TOKEN)
