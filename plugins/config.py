import re os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    API_ID = int(os.environ.get("API_ID", 13290427))

    API_HASH = os.environ.get("API_HASH", "c33b2f280810fc2f60a6387a4c4217f2")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1745243508").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @UploadLinkToFileBot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Aryan6969:Aryan6969@cluster0.krhmwhe.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001711211283)

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "1745243508"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "ary_botz")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "UploadLinkToFileBot")

    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))

    PRO_USERS.append(OWNER_ID)
