import allure
from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators

class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ConstructorLocators()
    
    @allure.step("Открыть страницу конструктора")
    def open(self):
        return self.open_page("main")
    
    @allure.step("Получить активный раздел")
    def get_active_section(self):
        active_section = self.find_element(self.locators.ACTIVE_SECTION)
        return active_section.text
    
    @allure.step("Кликнуть на раздел булок")
    def click_buns_section(self):
        self.click(self.locators.BUNS_SECTION)
        return self
    
    @allure.step("Кликнуть на раздел соусов")
    def click_sauces_section(self):
        self.click(self.locators.SAUCES_SECTION)
        return self
    
    @allure.step("Кликнуть на раздел начинок")
    def click_fillings_section(self):
        self.click(self.locators.FILLINGS_SECTION)
        return self