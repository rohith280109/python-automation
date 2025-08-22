import logging
import pytest
import yaml


from setup import get_driver
from selefunc import *

logger = logging.getLogger("pytestlogin")

with open("requ.yaml","r") as f:
    Req = yaml.safe_load(f)

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get(Req['url'])
    yield driver
    driver.quit()

def test_success_login(driver):

    logging.info("test case 1: valid login")
    login_user(driver, Req["users"][0]["username"], Req["users"][0]["password"], Req["locators"], logger)
    assert  flash_text(driver, Req["messages"]["success"], logger)
    logout_l(driver, Req["locators"], logger)
    logger.info("Test case 1 passed")

def test_invalid_username(driver):
    logger.info("Test case 2: Invalid username")
    login_user(driver, Req["users"][1]["username"], Req["users"][1]["password"], Req["locators"], logger)
    assert flash_text(driver, Req["messages"]["invalid_username"], logger)
    logger.info("Test case 2 passed")


def test_invalid_password(driver):
    logger.info("Test case 3: Invalid password")
    login_user(driver, Req["users"][2]["username"], Req["users"][2]["password"], Req["locators"], logger)
    assert flash_text(driver, Req["messages"]["invalid_password"], logger)
    logger.info("Test case passed")
