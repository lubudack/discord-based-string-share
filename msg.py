import discord
import json
import time

client = discord.Client()
print('discord-based server')

@client.event
async def on_message(message):
    while True:
        await message.channel.send('f')
        time.sleep(1)

client.run('NjI1MTI5Mjg4OTM2NzE4MzM2.XYbDBA.LRorQoNxEeAOqkgN0-nDlOQInAc')