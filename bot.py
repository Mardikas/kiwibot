import sys

sys.path.append('events')
sys.path.append('background')
sys.path.append('commands')

from discord.ext.commands import Bot
import token_read
import random
import requests

import commands
import event_handler
import background

BOT_PREFIX = ("?", "!", "Kiwi ", "kiwi")
token = token_read.read()

client = Bot(command_prefix=BOT_PREFIX)

commands.init_commands(client)
background.init_processes(client)
event_handler.init_events(client)

# in this files will be listed all commands that can be given to bot by users below are three example commands


client.run(token)
