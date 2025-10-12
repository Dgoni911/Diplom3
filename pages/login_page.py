from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from helpers.url_helper import UrlHelper

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = UrlHelper.get_url("login")
    
    def open(self):
        self.driver.get(self.url)
    
    def login(self, email, password):
        self.find_element(LoginLocators.EMAIL_INPUT).send_keys(email)
        self.find_element(LoginLocators.PASSWORD_INPUT).send_keys(password)
        self.click_element(LoginLocators.LOGIN_BUTTON)