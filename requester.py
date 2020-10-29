import discord
import json
import time
import os

client = discord.Client()

request = 'admin'
permis = ['user','admin']

@client.event
async def on_message(message):
    with open('reqf.txt', 'r', encoding='UTF8') as f:
        ff = f.read()
        try:
            if ff[0:3] == 'req':
                print('requested!')
                await message.channel.send('+req|' + request + '|' + ff[3:] + '|' + permis)
                with open('reqf.txt', 'w', encoding='UTF8') as w:
                    w.write('r syc')
                    print('req succful')
        except:
            pass
    if message.content.startswith('+sen') and message.content.split('|')[1] == request:
        print('sented:' , message.content.split('|')[2])
        rep = message.content.split('|')[2].replace("'", '"')
        with open('sentfile.json', 'w', encoding='UTF8') as w:
            w.write(rep)

client.run(os.environ['token'])
