# this parses a discord message and returns according request

import json
import random

commands = ['!help', '!hey', '!calc']


class Parse_result():

    def __init__(self):
        self.type = None
        self.data = []


def parse(message=None):
    parse_result = Parse_result()

    print('parsing content:', end=' ')
    print(message.content)
    words = message.content.split()
    if words[0] in commands:
        print('first word is', words[0])
        print(commands[1])
        parse_result.type = 'command'
    elif message.content.lower() in simple_replies:
        reply = simple_replies.get(message.content.lower())
        reply = reply[random.randint(0, len(reply) - 1)]
        parse_result.type = 'simple_reply'
        parse_result.data.append(reply)
    return (parse_result)


def load_simple_replies():
    # this loads simple replys from a file to a dictionary

    with open("simple_replies.json", 'r') as file:
        return json.loads(file.read())


simple_replies = load_simple_replies()
print(simple_replies)
