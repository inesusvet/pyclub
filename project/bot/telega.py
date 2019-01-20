import logging

from brain import Message

logger = logging.getLogger(__name__)


class TelegramAPI(object):
    def __init__(self, transport):
        self.transport = transport
        self.last_update_id = None

    def read(self, limit=0):
        updates = self.transport.get_updates(offset=self.last_update_id)
        if updates:
            self.last_update_id = max(up.update_id for up in updates) + 1

        messages = [
            Message(update.message.chat.id, update.message.text)
            for update in updates
            if update.message
        ]
        return messages

    def write(self, message):
        logger.debug('Sending a message to telegram %r', message)
        self.transport.send_message(
            message.channel,
            message.text,
        )


def open(token):
    import telegram

    client = telegram.Bot(token)
    return TelegramAPI(client)
