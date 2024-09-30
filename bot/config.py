from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 12411512))
    API_HASH = env.get("TELEGRAM_API_HASH", "0417d4f5fa67431b3c1b984a712cdbe3")
    OWNER_ID = int(env.get("OWNER_ID", 2113726835))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "2113726835").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "RssBotXBot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6730490066:AAEMtyTH4OlpS3o9JXdd1KXmF-WX99LB5Xo")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002113042652))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "http://46.4.113.153:9019")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 9019))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
