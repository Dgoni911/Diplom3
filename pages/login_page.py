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
        self.wait_for_page_loaded()
        
        email_locators = [
            self.locators.EMAIL_INPUT,
            self.locators.EMAIL_INPUT_ALT,
            self.locators.EMAIL_INPUT_ALT2,
            self.locators.EMAIL_INPUT_ALT3,
            self.locators.EMAIL_INPUT_ALT4
        ]
        
        for locator in email_locators:
            try:
                if self.is_visible(locator, timeout=2):
                    self.type_text(locator, email)
                    return self
            except:
                continue
        
        self.take_screenshot("login_email_not_found")
        raise Exception("Не удалось найти поле для ввода email")
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.wait_for_page_loaded()
        
        password_locators = [
            self.locators.PASSWORD_INPUT,
            self.locators.PASSWORD_INPUT_ALT,
            self.locators.PASSWORD_INPUT_ALT2
        ]
        
        for locator in password_locators:
            try:
                if self.is_visible(locator, timeout=2):
                    self.type_text(locator, password)
                    return self
            except:
                continue
        
        self.take_screenshot("login_password_error")
        raise Exception("Не удалось найти поле для ввода пароля")
    
    @allure.step("Кликнуть кнопку Входа")
    def click_login_button(self):
        login_button_locators = [
            self.locators.LOGIN_BUTTON,
            self.locators.LOGIN_BUTTON_ALT
        ]
        
        for locator in login_button_locators:
            try:
                if self.is_visible(locator, timeout=2):
                    self.click(locator)
                    self.wait_for_page_loaded()
                    return self
            except:
                continue
        
        self.take_screenshot("login_button_not_found")
        raise Exception("Не удалось найти кнопку входа")
    
    @allure.step("Выполнить полный логин")
    def complete_login(self, email, password):
        self.open()
        self.wait_for_page_loaded()
        self.wait.wait_for_element_visible(self.locators.LOGIN_FORM)
        
        return (self.enter_email(email)
                .enter_password(password)
                .click_login_button())
    
    @allure.step("Проверить наличие формы логина")
    def is_login_form_present(self):
        return self.is_visible(self.locators.LOGIN_FORM)
    
    @allure.step("Получить текст ошибки")
    def get_error_message(self):
        if self.is_visible(self.locators.ERROR_MESSAGE, timeout=3):
            return self.get_text(self.locators.ERROR_MESSAGE)
        return ""
    
    @allure.step("Проверить загрузку страницы логина")
    def is_login_page_loaded(self):
        return self.is_present(self.locators.LOGIN_FORM)