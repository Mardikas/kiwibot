# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py

# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import token_read
import sys
import message_handler
import asyncio

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
    await client.wait_until_ready()
    response = message_handler.message_handle(message, client.user)
    if response.should_respond is True:
        for msg in response.messages_to_send:
            await client.send_message(message.channel, msg)

    print('Messages received in current session', len(client.messages))


@client.event
async def on_ready():
    await client.wait_until_ready()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@asyncio.coroutine
async def connect():
    loop = asyncio.get_event_loop()
    try:
        print('Connecting to client...')
        client.start(TOKEN)
        await client.on_ready()
        # client.login(TOKEN)
        # client.connect()
        print("Success")
    except KeyboardInterrupt:
        loop.run_until_complete(client.logout())
    # finally:a
    #    loop.close()
    print("shouldn't reach here")


connect()
