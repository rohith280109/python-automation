import logging

logger = logging.getLogger("multilog3")

def multilogg3():
    logger.info('hello world')
    logger.critical("critical error")
    logger.error("this from multilog3")