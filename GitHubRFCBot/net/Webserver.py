from http.server import BaseHTTPRequestHandler
from io import BytesIO
from json import loads

from GitHubRFCBot.logger import logger
from GitHubRFCBot.net.DiscordNotification import DiscordNotification


class Webserver(BaseHTTPRequestHandler):
    def do_POST(self):
        discord_notification = DiscordNotification()
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        parsed_body = loads(body)

        action = parsed_body['action']

        # Check if the issue was created or not
        if action != 'opened':
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

        extracted_title = issue_title[4:].lstrip()
        topic_url = str(parsed_body['issue']['html_url'])
        author = str(parsed_body['issue']['user']['login'])
        profile_picture = str(parsed_body['issue']['user']['avatar_url'])

        logger.debug(f'Extracted title: {extracted_title}')

        # Issue is a "request for comments"
        logger.info(f'Publishing info to Discord')

        discord_notification.notify(
            str(extracted_title),
            topic_url,
            author,
            profile_picture
        )

        self.send_response(204)
        self.end_headers()
