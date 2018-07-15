import sys

sys.path.append('message_handler')

import message_handler

def init_events(client):
    @client.event
    async def on_ready():
        print("Logged in as " + client.user.name)

    print("event init successful!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        print("received a message!")

        response = message_handler.message_handle(message, client.user)
        if response.should_respond is True:
            for msg in response.messages_to_send:
                await client.send_message(message.channel, msg)
        await client.process_commands(message)
