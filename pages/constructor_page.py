from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators

class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_active_section(self):
        active_section = self.find_element(ConstructorLocators.ACTIVE_SECTION)
        return active_section.text
    
    def click_buns_section(self):
        self.click_element(ConstructorLocators.BUNS_SECTION)
    
    def click_sauces_section(self):
        self.click_element(ConstructorLocators.SAUCES_SECTION)
    
    def click_fillings_section(self):
        self.click_element(ConstructorLocators.FILLINGS_SECTION)