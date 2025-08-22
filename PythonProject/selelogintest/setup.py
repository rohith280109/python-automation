from selenium import webdriver
def get_driver():
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordGeneration,PasswordLeakDetection,PasswordLeakDetectionUnauthenticated,PasswordCheck")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver