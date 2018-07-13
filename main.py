# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py

# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import token_read
import sys
import parser

try:
    TOKEN = token_read.read()
except:
    print('Failed to read token')
    sys.exit(1)
else:
    print('Token read success!')

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
    print('Messages received in current session', len(client.messages))
    parser.parse(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.close()
print('Connecting to client...')
client.run(TOKEN)