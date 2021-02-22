#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
from sample_config import Config
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist

    if not os.path.isdir(Config.DOWNLOAD_LOCATIONs):
        os.makedirs(Config.DOWNLOAD_LOCATIONs)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "AnyDLBot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()

    Config.AUTH_USERS.add(683538773)
