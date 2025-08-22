import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()  # this is screen purpose
file_handler = logging.FileHandler("multilog.log")  # this creates file and stores the information
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.debug("just a debug msg")