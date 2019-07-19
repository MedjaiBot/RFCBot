import os
from sys import exit
from http.server import HTTPServer

from dotenv import load_dotenv
from GitHubRFCBot.logger import logger
from GitHubRFCBot.net import Webserver


class GitHubRFCBot:
    def run(self):
        logger.info('Starting application')

        logger.debug('Loading .env file')
        load_dotenv()
        logger.debug('Loaded .env file')

        self.run_webserver()

    def run_webserver(self):
        interface = os.environ['HTTP_INTERFACE']

        if 'PORT' in os.environ:
            port = int(os.environ['PORT'])
        else:
            port = int(os.environ['HTTP_PORT'])

        logger.info(f'Going to listen on {interface}:{port}')

        webserver = None

        try:
            webserver = HTTPServer(
                (interface, port), Webserver.Webserver
            )
            webserver.serve_forever()
        except OSError as exception:
            logger.error(
                'Port is already bound to another application. Exiting.'
            )
            exit(1)
        except KeyboardInterrupt:
            pass

        webserver.server_close()
        logger.info('Stopped webserver')
