from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_user(driver,username, password,locators,logger):

    driver.find_element(By.NAME,locators["username_input"]).send_keys(username)
    driver.find_element(By.NAME,locators["password_input"]).send_keys(password)
    login = driver.find_element(By.XPATH,locators["login_button"])
    driver.execute_script("arguments[0].click();", login)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID,"flash")
    ))
    logger.info("login attempted")

def flash_text(driver,secure_text,logger):


    secure = driver.find_element(By.ID, "flash").text
    if secure_text in secure:
        logger.info(f"flash msg matched to secure_text")
        return True
    else:
        logger.error(f"expected text {secure_text} but found {secure}")
        return False


def logout_l(driver,locators,logger):
    logout = driver.find_element(By.XPATH,locators["logout_button"] )
    driver.execute_script("arguments[0].click();", logout)
    logger.info("logout successfull")

