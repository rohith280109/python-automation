import logging
import yaml

from selefunc import *
from setup import get_driver

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename = "seletest.log",
    filemode = "w"
)
logger = logging.getLogger("selenium_tests")

with open("requ.yaml", 'r') as f:
    Req = yaml.safe_load(f)
driver = get_driver()
driver.get(Req["url"])


logger.info("Test case 1: Valid login")
login_user(driver,Req["users"][0]["username"],Req["users"][0]["password"],Req["locators"],logger)
a = flash_text(driver,Req["messages"]["success"],logger)
if a:
    logout_l(driver,Req["locators"],logger)
    logger.info("Test case 1 passed")
else:
    logger.error("Test case 1 failed")


logger.info("Test case 2: Invalid username")
login_user(driver,Req["users"][1]["username"],Req["users"][1]["password"], Req["locators"],logger)
a = flash_text(driver,Req["messages"]["invalid_username"],logger)
if a:
    logger.info("Test case 2 passed")
else:
    logger.error("Test case 2 failed")


logger.info("Test case 3: Invalid password")
login_user(driver,Req["users"][2]["username"],Req["users"][2]["password"], Req["locators"],logger)
a = flash_text(driver,Req["messages"]["invalid_password"],logger)
if a:
    logger.info("Test case 3 passed")
else:
    logger.error("Test case 3 failed")