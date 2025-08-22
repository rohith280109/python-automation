import logging

logger = logging.getLogger("multilog2")
logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

def multilogg2():
    logger.info("this from multilog2")
    logger.critical("critical error")
    logger.error("this from multilog2")
