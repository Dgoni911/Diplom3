from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from helpers.url_helper import UrlHelper

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = UrlHelper.get_url("feed")
    
    def open(self):
        self.driver.get(self.url)
    
    def get_total_orders_count(self):
        element = self.find_element(OrderFeedLocators.TOTAL_ORDERS)
        return int(element.text)
    
    def get_today_orders_count(self):
        element = self.find_element(OrderFeedLocators.TODAY_ORDERS)
        return int(element.text)
    
    def get_orders_in_progress(self):
        elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [elem.text for elem in elements]
    
    def get_latest_order_number(self):
        orders = self.find_elements(OrderFeedLocators.ORDER_ITEMS)
        if orders:
            order_number_element = orders[0].find_element(*OrderFeedLocators.ORDER_NUMBER)
            return order_number_element.text
        return None