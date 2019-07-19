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
        author_profile_picture_url: str,
        status: int
    ):
        logger.debug(f'Notifying with the following topic: {topic}')

        if status == 1:
            embed_description = DiscordNotification.get_opened_description(
                topic)

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
        elif status == 2:
            embed_description = DiscordNotification.get_closed_description(
                topic)

            embed = DiscordEmbed(
                title='A RFC was closed',
                description=embed_description,
                color=24566102
            )
            embed.set_author(
                name=author,
                url=topic_url,
                icon_url=author_profile_picture_url
            )
        else:
            embed_description = DiscordNotification.get_reopened_description(
                topic)

            embed = DiscordEmbed(
                title='A RFC was reopened',
                description=embed_description,
                color=2552470
            )
            embed.set_author(
                name=author,
                url=topic_url,
                icon_url=author_profile_picture_url
            )

        self.discord_webhook.add_embed(embed)
        self.discord_webhook.execute()

    @staticmethod
    def get_opened_description(topic: str):
        return '\n'.join([
            f'The RFC "{topic}" is now available for comments.',
            '',
            'If you would like to participate create an account on Github or discuss it in this channel.'
        ])

    @staticmethod
    def get_closed_description(topic: str):
        return '\n'.join([
            f'The RFC "{topic}" was closed.',
            '',
            'If you would like to say anything that is related to that topic, feel free to mention a maintainer that he reopens the discussion.'
        ])

    @staticmethod
    def get_reopened_description(topic: str):
        return '\n'.join([
            f'The RFC "{topic}" was reopened.',
            '',
            'If you would like to participate create an account on Github or discuss it in this channel.'
        ])
