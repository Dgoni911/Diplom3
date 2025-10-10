import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


class LoginPage(BasePage):
    
    @allure.step("Ввести email")
    def enter_email(self, email):
        email_input = self.find_element(LoginPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        password_input = self.find_element(LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
    
    @allure.step("Кликнуть кнопку входа")
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)
    
    @allure.step("Выполнить вход")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()