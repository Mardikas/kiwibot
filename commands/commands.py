import random
import requests


# in this files will be listed all commands that can be given to bot by users below are three example commands

def init_commands(client):
    @client.command()
    async def eigth_ball():
        responses = [
            'Thats bad',
            'Gonna be fine'
        ]
        await client.say(random.choice(responses))

    @client.command()
    async def bitcoin():
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        response = requests.get(url)
        value = response.json()['bpi']['USD']['rate']
        await client.say("Bitcoin price is: $" + value)
