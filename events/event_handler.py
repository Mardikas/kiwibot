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
        reply = 'received a message!'.format(message)
        await client.send_message(message.channel, reply)
        await client.process_commands(message)
