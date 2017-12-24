import BaseHTTPServer
import logging

logging.basicConfig(
    format='%(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

HOST = ''
PORT = 8000


class LoggingHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        logger.info('Imcoming request from %s', self.client_address)
        logger.info('%s %s', self.command, self.path)
        logger.info(self.headers)
        self.send_response(200)
        self.end_headers()

        self.wfile.write('Hello, world!')


def main():
    handler = LoggingHandler

    httpd = BaseHTTPServer.HTTPServer((HOST, PORT), handler)
    print 'Serving on port {}'.format(PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
