@title[title]
# Build your first slack bot in three hours

#### by Ivan Styazhkin @ DataRobot

---
@title[why]
## Why?
> Ensure happiness and productivity of your colleagues

![Give tools to the people!](https://github.com/inesusvet/pyclub/raw/master/assets/tools-to-the-people.png)

---
## Reference

- Slack API `https://api.slack.com/methods`
- Python Slack Client `https://github.com/slackapi/python-slackclient`

---
@title[register]
### Register a new bot

https://datarobot.slack.com/apps/manage/custom-integrations

---
@title[setup]
### Setup an environment

- Extract an archive to directory A
- Change work directory to the directory A
- Execute smoke-test `venv/bin/python -c 'import slackclient; print "OK"'`

---
### Bootstrap

- Create new python file
- Run it

---
### Connect to Slack

- Import `slackclient`
- Initialize `slackclient.SlackClient` object
- Run it!

+++
### Connect to Slack

- Try to connect with `.rtm_connect()` call
- Save user ID from `.api_call('auth.test')` call
- Run it!

+++
### Connected!

- Bot is online while this python script runs
- ...
- PROFIT!

---
### Listen to events

- One `read` and one `print` per script run
- Run it!

+++
### Listen to events

- Wrap `read()` into endless `while` cycle
- Run it!
- Stop it by `Ctrl + C`

---
### Distinguish addressed messages

- Create a function which checks substring
- Print out only addressed messages now
- Test it!

---
### Extract a command

- Threat first word as a command
- Print only messages with a specific command
- Test it!
- Extra: _Extract author's name from the message_

---
### Compose an answer

- Create a function with hardcoded answer
- Make an echo-function
- Test the function!

---
### Send answer back

- Extract a channel ID from the message
- Use `.api_call('chat.postMessage', ...)` call
- Test it!

---
### Repeat

- Add two more commands and new responses
- Test it!

---
# Just did it

Hip-hip, Hooray!
