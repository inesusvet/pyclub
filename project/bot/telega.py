import collections
import logging

from brain import Message

logger = logging.getLogger(__name__)


class TelegramAPI(object):
    def __init__(self, bot):
        self.bot = bot
        self.last_update_id = 0

    def read(self, limit=0):
        updates = self.bot.get_updates(offset=self.last_update_id)

        messages = []
        for update in updates:
            logger.debug('Getting an update: %s', update)
            self.last_update_id = update.update_id
            if not update.message:
                continue

            channel = update.message.chat.id
            text = update.message.text
            messages.append(Message(channel, text))

        self.last_update_id += 1
        return messages

    def write(self, message):
        logger.debug('Sending a message to telegram %r', message)
        self.bot.send_message(
            message.channel,
            message.text,
        )


def open(token):
    import telegram

    client = telegram.Bot(token)
    return TelegramAPI(client)
