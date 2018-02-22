"""The `noname_pi_bot` main module."""

import os
import requests
import logging

from requests import codes

from telegram.ext import Updater, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

token = os.environ['TOKEN']
updater = Updater(token=token)


def start(bot, update):
    """Handle the `start` command."""
    bot.send_message(
        chat_id=update.message.chat_id,
        text="All right! You don't have to shout at me!!",
    )


def ip(bot, update):
    """Handle the `ip` command.

    Retrieve the external IP of this bot by querying some shady website
    and parsing its JSON response. Report the IP to the user.
    """
    url = 'https://api.ipify.org?format=json'
    resp = requests.get(url)
    if resp.status_code != codes.OK:
        message = \
            "Could not get external ip address from this URL: `{url}`." \
            "It's response code was `{code}`" \
            .format(url=url, code=resp.status_code)
        logging.fatal(message)
        bot.send_message(
            chat_id=update.message.chat_id,
            parse_mode="Markdown",
            text=message,
        )
        return

    ip = resp.json()['ip']
    bot.send_message(
        chat_id=update.message.chat_id,
        parse_mode="Markdown",
        text="My external IP is `{ip}`".format(ip=ip),
    )


start_handler = CommandHandler('start', start)
ip_handler = CommandHandler('ip', ip)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(ip_handler)

updater.start_polling()
