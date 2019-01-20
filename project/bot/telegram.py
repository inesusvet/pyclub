
class TelegramAPI(object):
    def __init__(self, token):
        self.token = token

    def read(self):
        return []


def get_transport(token):
    return TelegramAPI(token)
