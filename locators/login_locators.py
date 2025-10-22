from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and contains(@name, 'email')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGIN_FORM = (By.XPATH, "//form[contains(@class, 'Auth_form')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")
    
    EMAIL_INPUT_ALT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT_ALT = (By.XPATH, "//input[@name='password']")
    EMAIL_INPUT_ALT2 = (By.CSS_SELECTOR, "input[type='text']")
    PASSWORD_INPUT_ALT2 = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON_ALT = (By.CSS_SELECTOR, "button[type='submit']")
    
    EMAIL_INPUT_ALT3 = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    EMAIL_INPUT_ALT4 = (By.XPATH, "//input[contains(@placeholder, 'email') or contains(@placeholder, 'Email')]")