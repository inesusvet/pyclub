import os

from slackclient import SlackClient


def main(slack_token):
    print 'Yay!', slack_token
    # Initialize object with a token
    slack_client = SlackClient(slack_token)
    print 'Initialized'


if __name__ == '__main__':
    slack_token = os.environ.get('SLACK_TOKEN', '<your-token-here>')
    exit(main(slack_token))
