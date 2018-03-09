import os
import pprint

from slackclient import SlackClient


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

    events = slack_client.rtm_read()  # Check for new messages
    if not events:
        print 'No new events for me'
        return 0

    else:
        print 'Fetched', len(events), 'events'
        for event in events:
            pprint.pprint(event)


if __name__ == '__main__':
    slack_token = os.environ.get('SLACK_TOKEN', '<your-token-here>')
    exit(main(slack_token))
