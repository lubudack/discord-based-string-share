import discord
import json
import os

client = discord.Client()
print('discord-based server')

@client.event
async def on_message(message):
    if message.content.startswith('+req'):
        sp = message.content.split('|')
        print('user[', sp[1], '](permit[', sp[3], '])', sp[2] + '.json requested!')
        w = open('/sendto/' + sp[2] + '.json', 'r', encoding='UTF8')
        r = json.load(w)
        try:
            f = r['permit']
            print('permi', sp[3] , '=', r['permit'], '?')
            if f in sp[3]:
                print('permission allowed!')
                await message.channel.send('+sen|' + sp[1] + '|' + str(r))
            else:
                print('denied!')
        except KeyError:
            await message.channel.send('+sen|' + sp[1] + '|' + str(r))
        w.close()

client.run(os.environ['token'])
