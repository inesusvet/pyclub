import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world'


@app.route('/<slug>')
def get(slug):
    return 'nothing to show for {}'.format(slug), 404


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
