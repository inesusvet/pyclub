import flask

app = flask.Flask(__name__, template_folder='.')


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/<slug>')
def get(slug):
    return 'nothing to show for {}'.format(slug), 404


@app.route('/', methods=['POST'])
def post():
    form = flask.request.form
    if 'url' not in form:
        flask.abort(400, 'url parameter is required')

    return form['url']


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
