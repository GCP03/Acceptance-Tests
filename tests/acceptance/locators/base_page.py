from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'h1'
    # tuple, same as TITLE = (By.TAG_NAME, 'h1')