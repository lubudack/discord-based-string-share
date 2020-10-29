import discord
import json
import time
import os

client = discord.Client()
print('discord-based server')

@client.event
async def on_message(message):
    while True:
        await message.channel.send('f')
        time.sleep(1)

client.run(os.environ['token'])
