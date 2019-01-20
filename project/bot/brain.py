import logging

logger = logging.getLogger(__name__)


class Message(object):
    def __init__(self, channel, text):
        self.channel = channel
        self.text = text

    def __repr__(self):
        return '<Mesage in %s: "%s">' % (self.channel, self.text)


def echo(incoming, outgoing):
    """
    Simple move all messages from incoming queue to outgoing queue
    """
    outgoing.extend(incoming)
    incoming.clear()


def process(incoming, outgoing):
    return echo(incoming, outgoing)
