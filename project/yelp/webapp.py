import os

import codecs
from datetime import date, timedelta

from flask import Flask, redirect, request

from main import load_feedback, save_feedback, add_comment, search_for_date

app = Flask(__name__)

FILENAME = 'feedback.json'


def save_new_comment(author, comment):
    feedback = load_feedback(FILENAME)
    add_comment(feedback, author, comment)
    save_feedback(feedback, FILENAME)


@app.route("/")
def hello():
    with open('home.html') as file_obj:
        return file_obj.read()


@app.route("/submit", methods=['POST'])
def submit():
    data = request.form
    if 'hate' not in data and 'like' not in data:
        return redirect("/", code=302)


    comment = data.get('comment', '')
    author = data.get('author', '')
    if not author:
        author = 'Anonymous'
    result = 'Hate! ' + comment if 'hate' in data else 'Like! ' + comment
    save_new_comment(author, result)
    with open('thanks.html') as file_obj:
        return file_obj.read()


@app.route('/daily')
def daily():
    with codecs.open('daily.html', encoding='utf-8') as file_obj:
        TEMPLATE = file_obj.read()

    today = date.today()
    all_feedback = load_feedback(FILENAME)
    today_comments = search_for_date(all_feedback, today)
    result = u''
    for item in today_comments:
        result += u'<li>{}: {}</li>'.format(item['author'], item['comment'])

    if result == u'':
        return TEMPLATE.format('Sorry, there are no comments yet :(')

    return TEMPLATE.format(result)


@app.route('/weekly')
def weekly():
    all_feedback = load_feedback(FILENAME)
    result = []

    one_week_ago = date.today() - timedelta(days=7)
    for offset in range(8):
        day = one_week_ago + timedelta(days=offset)
        this_week_comments = search_for_date(all_feedback, day)
        for item in this_week_comments:
            result_string = u'<li>{2}: {0} - {1}</li>'.format(
                item['author'],
                item['comment'],
                item['added_at'][:10],
            )
            result.append(result_string)

    with codecs.open('daily.html', encoding='utf-8') as file_obj:
        TEMPLATE = file_obj.read()
    if result == []:
        return TEMPLATE.format('Sorry, there are no comments for this week :(')
    return TEMPLATE.format(''.join(result[::-1]))


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
