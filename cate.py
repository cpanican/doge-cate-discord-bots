import config
import discord
import asyncio
import clever as cl

clever = cl.CleverBot(user=config.API_CLEVERBOT_USER, key=config.API_CLEVERBOT_KEY, nick='cate')
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if (client.user.id != message.author.id) and (message.author.id == '444656539593343006'):
        if message.content.startswith('!test'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await client.edit_message(tmp, 'You have {} messages.'.format(counter))

        elif message.content.startswith('!sleep'):
            await asyncio.sleep(5)
            await client.send_message(message.channel, 'Done sleeping')

        else:
            await client.send_message(message.channel, clever.query(message.content))

client.run(config.CATE_DISCORD_TOKEN)