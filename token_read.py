class TokenError(RuntimeError):
    pass

def read() -> str:
    with open('TOKEN.txt', 'r') as file:
        print('opening TOKEN file')
        TOKEN = file.read()

    try:
        assert(len(TOKEN)==59)
    except AssertionError:
        print('Token lenght unfitting!', len(TOKEN))
        return False
    return TOKEN