import discord
import asyncio
import datetime
from discord.ext import tasks

client = discord.Client()

@client.event
async def on_ready():
    loop.start()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

n_time=datetime.datetime.now()
@tasks.loop(seconds=60)
async def loop():
    if not client.is_ready():
        return
    c_time="22:50"
    if n_time.weekday()==1:
        if n_time.strftime('%H:%M')==c_time:
            channel_id = client.get_channel(721738331968241752)
            await channel_id.send('みんな会議だよ\tしゅーごー')
#    if message.content.startswith('今何時？'):
#        await client.send_message(message.channel, n_time.time())
@client.event
async def on_message(message):
    if message.content.startswith('今何時？'):
        await client.send_message(message.channel, n_time.time())

client.run('NDY2NDAyODQyNTAwOTIzMzky.DimuMQ.zWnIzerHztwo_rHnqRhvqB68GdE')
