import logging
from logging.handlers import RotatingFileHandler

# create logger
logger = logging.getLogger("rotating_logger")
logger.setLevel(logging.DEBUG)

# rotating file handler (max 1 KB per file, keep 3 backups)
handler = RotatingFileHandler("rotating.log", maxBytes=1024, backupCount=3)

# formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

# generate lots of logs
for i in range(88):
    logger.info("Message number %d", i)
