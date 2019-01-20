import collections
import logging
import sys
import time

import brain

logger = logging.getLogger(__name__)


def main(transport, incoming, outgoing):
    logger.info('Staring infinite loop')
    while True:
        new_messages = transport.read()
        if not new_messages:
            logger.debug('No new messages. Sleeping five seconds')
            time.sleep(5)
            continue

        incoming.extend(new_messages)
        logger.debug('Passing %d messages to the Inbox', len(incoming))

        brain.process(incoming, outgoing)

        logger.debug('Passing %d messages to the Send', len(outgoing))
        while len(outgoing) > 0:
            message = outgoing.popleft()
            logger.debug('Sending a message: %s', message.text)
            transport.write(message)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError('Need a transport name and the token')

    _, transport_name, token = sys.argv[:3]

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s\t%(levelname)s\t%(message)s'
    )

    if transport_name == 'telegram':
        import telega
        transport = telega.open(token)
    elif transport_name == 'slack':
        import slack
        transport = slack.open(token)

    in_queue = collections.deque()
    out_queue = collections.deque()

    try:
        main(transport, in_queue, out_queue)
    except KeyboardInterrupt:
        logger.error('Stopping the process by KeyboardInterrupt')
        transport.close()

    except Exception as ex:
        logger.exception('Fatal failure')
        exit(1)
