import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('好きだよ'):
        counter = 0
        tmp = await client.send_message(message.channel, '私も好き')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('一緒に寝よ'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'ちょっと恥ずかしいよ')

client.run('token')
