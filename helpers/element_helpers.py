import allure
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from helpers.wait_helpers import WaitHelpers


class ElementHelpers:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelpers(driver)
    
    @allure.step("Получить текст элемента")
    def get_element_text(self, locator, timeout=10):
        element = self.wait.wait_for_element(locator, timeout)
        return element.text.strip()
    
    @allure.step("Ввести текст в поле")
    def safe_send_keys(self, locator, text, timeout=10, clear_first=True):
        element = self.wait.wait_for_element(locator, timeout)
        
        if clear_first:
            element.clear()
        
        element.send_keys(text)
        return element
    
    @allure.step("Получить атрибут элемента")
    def get_attribute(self, locator, attribute, timeout=10):
        element = self.wait.wait_for_element(locator, timeout)
        return element.get_attribute(attribute)
    
    @allure.step("Проверить активность элемента")
    def is_element_enabled(self, locator, timeout=5):
        try:
            element = self.wait.wait_for_element(locator, timeout)
            return element.is_enabled()
        except TimeoutException:
            return False
    
    @allure.step("Проверить выделение элемента")
    def is_element_selected(self, locator, timeout=5):
        try:
            element = self.wait.wait_for_element(locator, timeout)
            return element.is_selected()
        except TimeoutException:
            return False
    
    @allure.step("Получить CSS свойство")
    def get_css_value(self, locator, property_name, timeout=10):
        element = self.wait.wait_for_element(locator, timeout)
        return element.value_of_css_property(property_name)