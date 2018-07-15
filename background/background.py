import asyncio


def init_processes(client):
    def display_heartbeat():
        print("HEARTBEAT:")
        if client.is_logged_in:
            print("Bot logged in")
            list_servers()
        else:
            print("Bot offline :( ")
            print("-------------")

    def list_servers():
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        print("-----------------")

    async def heartbeat():
        while (True):
            display_heartbeat()
            await asyncio.sleep(10)

    client.loop.create_task(heartbeat())
