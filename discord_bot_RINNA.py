import discord
import asyncio
from discord.ext import tasks
from login_chousei import chousei
import datetime

client = discord.Client()
@client.event
async def on_ready():
    loop.start()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
@client.event
async def on_message(message):
    n_time = datetime.datetime.now()
    if message.content.startswith('今何時？'):
        await message.channel.send(n_time.strftime('%H:%M'))
@tasks.loop(seconds=60)
async def loop():
    channel_id = client.get_channel(721738331968241752)
    if not client.is_ready():
        return
    c_time="22:50"
    n_time = datetime.datetime.now()
    if n_time.weekday()==6:
        if n_time.strftime('%H:%M')==c_time:
            await channel_id.send(chousei())
    if n_time.weekday()==1:
        if n_time.strftime('%H:%M')==c_time:
            await channel_id.send('説アレキだよ\tしゅーごー')
client.run('NDY2NDAyODQyNTAwOTIzMzky.DimuMQ.zWnIzerHztwo_rHnqRhvqB68GdE')
