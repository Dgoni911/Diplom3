from selenium.webdriver.common.by import By

class BaseLocators:
    LOADER = (By.XPATH, "//*[contains(@class, 'loader')]")
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")