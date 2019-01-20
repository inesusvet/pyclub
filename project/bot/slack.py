
class SlackAPI(object):
    def __init__(self, token):
        self.token = token

    def read(self):
        return []


def get_transport(token):
    return SlackAPI(token)
