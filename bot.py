import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from NaysaEncoderBot.config import Config

if __name__ == "__main__" :
    plugins = dict(
        root="NaysaEncoderBot"
    )
    naysabots = Client(
        "Id Finder Bot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100
    )
    naysabots.run()
