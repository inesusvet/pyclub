from flask import Flask, request, redirect

import core
import storage

HTML = """
<html>
  <head>
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet">
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
  </head>

  <body>
    <h1>Shorten your URL here</h1>

    <form method=post>
        <input name=url type=text size=50 />
        <input type=submit />
    </form>
  </body>
</html>
"""

app = Flask(__name__)


@app.route('/')
def home():
    return HTML


@app.route('/', methods=['POST'])
def to_short():
    url = request.form['url']
    already_existing_id = storage.find(url)
    if already_existing_id:
        return storage.get(already_existing_id)

    link_id = storage.put(url)
    slug = core.encode(link_id)
    return '<a href="%s">%s</a>' % (slug, slug)


@app.route('/<slug>')
def redirect_to_original(slug):
    print slug
    number = core.decode(slug)
    original_link = storage.get(number)
    return redirect("http://%s" % original_link)
