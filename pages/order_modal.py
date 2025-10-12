from pages.base_page import BasePage
from locators.order_modal_locators import OrderModalLocators

class OrderModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_order_number(self):
        return self.find_element(OrderModalLocators.ORDER_NUMBER).text
    
    def close_modal(self):
        self.close_modal()
    
    def is_visible(self):
        return self.is_element_present(OrderModalLocators.MODAL)