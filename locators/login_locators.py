from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGIN_FORM = (By.XPATH, "//form[contains(@class, 'Auth_form')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")