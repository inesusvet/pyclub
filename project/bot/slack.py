import logging

from brain import Message

logger = logging.getLogger(__name__)


class SlackAPI(object):
    def __init__(self, transport):
        self.transport = transport
        # Won't receive any messages if not authorized
        self.bot_id = self.transport.api_call('auth.test')['user_id']

    def read(self, limit=0):
        events = self.transport.rtm_read()
        logger.debug('Received %d events', len(events))
        messages = [
            Message(event['channel'], event['text'])
            for event in events
            if ('channel' in event and 'text' in event)
        ]
        return messages

    def write(self, message):
        self.transport.api_call(
            'chat.postMessage',
            channel=message.channel,
            text=message.text,
            as_user=True,
        )


def open(token):
    import slackclient
    client = slackclient.SlackClient(token)
    # Connect to Slack API
    # https://slackapi.github.io/python-slackclient/
    is_connected = client.rtm_connect(with_team_state=False)
    if not is_connected:
        raise RuntimeError('Failed to connect to slack')

    return SlackAPI(client)
