import collections
import logging
import sys

import brain

logger = logging.getLogger(__name__)


def main(transport, incoming, outgoing):
    logger.info('Staring infinite loop')
    while True:
        new_messages = transport.read()
        incoming.extend(new_messages)

        brain.process(incoming, outgoing)

        while len(outgoing) > 0:
            to_send = outgoing.pop(0)
            transport.write(to_send)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError('Need a transport name and the token')

    _, transport_name, token = sys.argv[:3]

    logging.basicConfig(level=logging.INFO)

    if transport_name == 'telegram':
        import telegram
        transport = telegram.get_transport(token)
    elif transport_name == 'slack':
        import slack
        transport = slack.get_transport(token)

    in_queue = collections.deque()
    out_queue = collections.deque()

    try:
        return_code = main(transport, in_queue, out_queue)
    except KeyboardInterrupt:
        logger.error('Stopping the process by KeyboardInterrupt')
    except Exception as ex:
        logger.exception('Fatal failure')
        exit(1)
