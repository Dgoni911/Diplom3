import allure
from helpers.wait_helper import WaitHelper
from helpers.url_helper import UrlHelper
from locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)
        self.url_helper = UrlHelper()
    
    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get(self.url_helper.get_url("login"))
        self.wait.wait_for_page_load()
        return self
    
    @allure.step("Ввести email {email}")
    def enter_email(self, email):
        email_field = self.wait.wait_for_element_visible(LoginLocators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)
    
    @allure.step("Ввести пароль {password}")
    def enter_password(self, password):
        password_field = self.wait.wait_for_element_visible(LoginLocators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
    
    @allure.step("Кликнуть кнопку Входа")
    def click_login_button(self):
        self.wait.wait_for_element_clickable(LoginLocators.LOGIN_BUTTON).click()
        self.wait.wait_for_page_load()