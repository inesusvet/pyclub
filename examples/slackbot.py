import os
import pprint
import time

from slackclient import SlackClient


def parse(event, bot_id):
    if event["type"] != "message":
        return
    elif "subtype" in event:
        return

    return bot_id in event['text']


def detect_command(message):
    words = message.split(' ')
    return words[0]


def bark(message):
    return 'Gav-gav! :doge:'


def echo(message):
    return message


def main(slack_token):
    print 'Yay!', slack_token
    # Initialize object with a token
    slack_client = SlackClient(slack_token)
    print 'Initialized'

    # Connect to Slack API
    # https://slackapi.github.io/python-slackclient/
    is_connected = slack_client.rtm_connect(with_team_state=False)
    if not is_connected:
        print 'Failed to connect to slack'
        return 1
    print 'Connected'

    # Save user ID to detect messages addressed to the bot
    bot_id = slack_client.api_call('auth.test')['user_id']
    print 'Authorized as', bot_id

    while True:
        events = slack_client.rtm_read()  # Check for new messages
        if not events:
            print 'No new events for me'
            time.sleep(1)
            continue

        print 'Fetched', len(events), 'events'
        for event in events:
            is_addressed_to_me = parse(event, bot_id)
            if is_addressed_to_me:
                text = event['text']
                channel = event['channel']
                if detect_command(text) == 'bark':
                    print 'Bark command is detected!'
                    answer = bark(text)
                    slack_client.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text=answer,
                    )


if __name__ == '__main__':
    slack_token = os.environ.get('SLACK_TOKEN', '<your-token-here>')
    exit(main(slack_token))
