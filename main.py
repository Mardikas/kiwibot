# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py

# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import token_read
import sys
import message_handler

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
    response = message_handler.message_handle(message, client.user)
    if response.should_respond is True:
        for msg in response.messages_to_send:
            await client.send_message(message.channel, msg)

    print('Messages received in current session', len(client.messages))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.close()
print('Connecting to client...')
client.run(TOKEN)
