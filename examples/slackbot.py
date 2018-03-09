import os


def main(slack_token):
    print 'Yay!', slack_token


if __name__ == '__main__':
    slack_token = os.environ.get('SLACK_TOKEN', '<your-token-here>')
    exit(main(slack_token))
