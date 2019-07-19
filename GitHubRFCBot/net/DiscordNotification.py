import os

from GitHubRFCBot.logger import logger
from discord_webhook import DiscordWebhook, DiscordEmbed


class DiscordNotification:
    def __init__(self):

        if not 'DISCORD_WEBHOOK_URL' in os.environ:
            logger.error('Could not find webhook url')

        self.notification_url = os.environ['DISCORD_WEBHOOK_URL']
        self.discord_webhook = DiscordWebhook(
            self.notification_url
        )

    def notify(
        self,
        topic: str,
        topic_url: str,
        author: str,
        author_profile_picture_url: str
    ):
        logger.debug(f'Notifying with the following topic: {topic}')

        embed_description = DiscordNotification.get_embed_description(topic)

        embed = DiscordEmbed(
            title='A new RFC is available',
            description=embed_description,
            color=5020550
        )
        embed.set_author(
            name=author,
            url=topic_url,
            icon_url=author_profile_picture_url
        )

        logger.debug(embed)
        logger.debug(embed.author)
        logger.debug(embed.title)
        logger.debug(embed.description)
        logger.debug(embed.color)

        self.discord_webhook.add_embed(embed)
        self.discord_webhook.execute()

    @staticmethod
    def get_embed_description(topic: str):
        return '\n'.join([
            f'The RFC "{topic}" is now available for comments.',
            '',
            'If you would like to participate create an account on Github or discuss it in this channel.'
        ])
