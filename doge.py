import config
import discord
import asyncio
import clever as cl

clever = cl.CleverBot(user=config.API_CLEVERBOT_USER, key=config.API_CLEVERBOT_KEY, nick='doge')
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if message.content == "abby is a":
            await client.send_message(message.channel, "paggot :rage:")

        elif message.content == "doge is a":
            await client.send_message(message.channel, "god :bow:")

        elif message.content == "where's the bots (╯°□°）╯︵ ┻━┻":
            await client.send_message(message.channel, "┬─┬ ノ( ゜-゜ノ)")

        elif message.content == "rage":
            await client.send_message(message.channel, "why u angry :rage:")

        elif message.content == "paggot":
            await client.send_message(message.channel, "ka :@")

        elif message.content.startswith('!test'):
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

client.run(config.DOGE_DISCORD_TOKEN)