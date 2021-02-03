import discord
import sys
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    n=random.randint(1,25)
    if(n==3 or n==18 or n==24 or n==11 or n==7):
        await message.channel.send("それじゃあダメなんよ")

client.run("********************************************")