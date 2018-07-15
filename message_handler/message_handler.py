import messageparser


class Response:
    def __init__(self):
        self.should_respond = False
        self.messages_to_send = []


def message_handle(message, kiwi):
    response = Response()
    # we do not want the bot to reply to itself
    if message.author == kiwi:
        return response

    action = messageparser.parse(message)
    if action.type == 'simple_reply':
        response.messages_to_send.append(action.simple_reply)
        response.should_respond = True
    # if message.content.startswith('!hello'):
    #    response.messages_to_send.append('Hello {0.author.mention}'.format(message))
    #  #response.messages_to_send.append('Hello {0.author.mention}')
    #   response.should_respond = True
    return response
