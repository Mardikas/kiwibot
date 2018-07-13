# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import parser

# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord

TOKEN =

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        await client.send_message(message.channel, 'whats up')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)