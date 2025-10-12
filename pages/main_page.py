from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_modal_locators import OrderModalLocators
from locators.login_locators import LoginLocators
from helpers.url_helper import UrlHelper
import time

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = UrlHelper.get_url("main")
        self.locators = MainPageLocators()
    
    def open(self):
        self.driver.get(self.url)
        self.wait_for_page_loaded()
    
    def wait_for_page_loaded(self):
        self.find_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
    
    def click_personal_account(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        time.sleep(2)
    
    def click_ingredient(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", ingredients[index])
            time.sleep(0.5)
            ingredients[index].click()
            self.wait_for_element_visible(OrderModalLocators.INGREDIENT_DETAILS, timeout=5)
    
    def get_ingredient_counter(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            counter_elements = ingredients[index].find_elements(*MainPageLocators.INGREDIENT_COUNTER)
            if counter_elements:
                return int(counter_elements[0].text)
        return 0
    
    def is_ingredient_modal_visible(self):
        return self.is_element_present(OrderModalLocators.INGREDIENT_DETAILS, timeout=3)
    
    def close_ingredient_modal(self):
        return self.close_modal()
    
    def click_make_order(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)
    
    def click_buns_section(self):
        self.click_element(MainPageLocators.BUNS_SECTION)
    
    def click_sauces_section(self):
        self.click_element(MainPageLocators.SAUCES_SECTION)
    
    def click_fillings_section(self):
        self.click_element(MainPageLocators.FILLINGS_SECTION)