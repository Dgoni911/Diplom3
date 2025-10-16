import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators()
    
    @allure.step("Открыть страницу логина")
    def open(self):
        return self.open_page("login")
    
    @allure.step("Ввести email")
    def enter_email(self, email):
        self.type_text(self.locators.EMAIL_INPUT, email)
        return self
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.type_text(self.locators.PASSWORD_INPUT, password)
        return self
    
    @allure.step("Кликнуть кнопку Входа")
    def click_login_button(self):
        self.click(self.locators.LOGIN_BUTTON)
        return self.wait_for_page_loaded()
    
    @allure.step("Выполнить полный логин")
    def complete_login(self, email, password):
        return (self.open()
                .enter_email(email)
                .enter_password(password)
                .click_login_button())
    
    @allure.step("Проверить наличие формы логина")
    def is_login_form_present(self):
        return self.is_visible(self.locators.LOGIN_FORM)
    
    @allure.step("Получить текст ошибки")
    def get_error_message(self):
        if self.is_visible(self.locators.ERROR_MESSAGE):
            return self.get_text(self.locators.ERROR_MESSAGE)
        return ""
    
    @allure.step("Проверить загрузку страницы логина")
    def is_login_page_loaded(self):
        return self.is_present(self.locators.LOGIN_FORM)