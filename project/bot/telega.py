import collections
import logging

from brain import Message

logger = logging.getLogger(__name__)


class TelegramAPI(object):
    def __init__(self, updater):
        self.updater = updater
        self.buffer = collections.deque()

    def on_message(self, message):
        logger.info('Saving message to buffer: %s', message)
        self.buffer.append(message)

    def read(self, limit=0):
        messages = []
        while len(self.buffer):
            logger.info('Getting message from buffer')
            update = self.buffer.popleft()

            channel = update['chat']['id']
            text = update['text']
            messages.append(Message(channel, text))

        return messages

    def write(self, message):
        logger.info('Sending a message to telegram %r', message)
        self.updater.bot.send_message(
            message.channel,
            message.text,
        )

    def close(self):
        self.updater.stop()


def open(token):
    from telegram.ext import Updater, MessageHandler

    updater = Updater(token)
    transport = TelegramAPI(updater)

    def callback(bot, update):
        transport.on_message(update.message)

    updater.dispatcher.add_handler(MessageHandler([], callback))

    updates = updater.start_polling(poll_interval=0.5, bootstrap_retries=0)

    return transport
