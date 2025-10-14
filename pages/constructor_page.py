import allure
from selenium.webdriver.common.by import By
from helpers.wait_helper import WaitHelper
from helpers.url_helper import UrlHelper
from locators.constructor_locators import ConstructorLocators

class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)
        self.url_helper = UrlHelper()
    
    @allure.step("Открыть страницу конструктора")
    def open(self):
        self.driver.get(self.url_helper.get_base_url())
        self.wait.wait_for_page_ready()
        return self
    
    @allure.step("Получить активный раздел")
    def get_active_section(self):
        active_section = self.wait.wait_for_element_visible(ConstructorLocators.ACTIVE_SECTION)
        return active_section.text
    
    @allure.step("Кликнуть на раздел булок")
    def click_buns_section(self):
        self.wait.wait_for_element_clickable(ConstructorLocators.BUNS_SECTION).click()
    
    @allure.step("Кликнуть на раздел соусов")
    def click_sauces_section(self):
        self.wait.wait_for_element_clickable(ConstructorLocators.SAUCES_SECTION).click()
    
    @allure.step("Кликнуть на раздел начинок")
    def click_fillings_section(self):
        self.wait.wait_for_element_clickable(ConstructorLocators.FILLINGS_SECTION).click()
    
    @allure.step("Проверить наличие элемента {locator}")
    def is_element_present(self, locator, timeout=5):
        try:
            self.wait.wait_for_element_present(locator, timeout)
            return True
        except:
            return False