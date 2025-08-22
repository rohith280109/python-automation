import logging
import multilog2
import multilog3

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename = "multiple.logs",
    filemode = "w"  # for append "a"
)

logger = logging.getLogger("multilog1")
logger.info("this is from multilog1")

multilog2.multilogg2()
multilog3.multilogg3()
