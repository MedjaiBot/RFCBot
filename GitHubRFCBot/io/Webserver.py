from http.server import BaseHTTPRequestHandler
from io import BytesIO
from json import loads

from GitHubRFCBot.logger import logger


class Webserver(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        parsed_body = loads(body)

        action = parsed_body['action']

        # Check if the issue was created or not
        if action != 'created':
            self.send_response(204)
            self.end_headers()
            return

        # Get the title of the issue
        issue_title = str(parsed_body['issue']['title'])

        # Check if the title of the issue starts with "RFC:"
        if not issue_title.startswith('RFC:'):
            self.send_response(204)
            self.end_headers()
            return

        # Issue is a "request for comments"
        logger.info(f'Publishing info to Discord')

        self.send_response(204)
        self.end_headers()
