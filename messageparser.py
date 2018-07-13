#this parses a discord message and returns according request
commands = ['!help', '!hey', '!calc']

def parse(message=None):


    print('parsing content:', end=' ')
    print(message)
    words = message.content.split()
    if words[0] in commands:
        print('first word is',words[0])
        print(commands[1])
