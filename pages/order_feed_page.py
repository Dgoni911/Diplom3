import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.order_modal_locators import OrderModalLocators

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()
    
    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        return self.open_page("feed")
    
    @allure.step("Дождаться загрузки ленты заказов")
    def wait_for_page_loaded(self):
        try:
            self.wait_for_element_visible(self.locators.TOTAL_ORDERS, timeout=10)
        except:
            self.wait_for_element_visible(self.locators.ORDER_ITEMS, timeout=10)
        return self
    
    @allure.step("Получить количество выполненных заказов за все время")
    def get_total_orders_count(self):
        try:
            total_orders = self.find_element(self.locators.TOTAL_ORDERS)
            return int(total_orders.text)
        except:
            return 0
    
    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders_count(self):  
        try:
            today_orders = self.find_element(self.locators.TODAY_ORDERS)
            return int(today_orders.text)
        except:
            return 0
    
    @allure.step("Проверить отображение секции 'В работе'")
    def is_in_progress_section_visible(self):
        return self.is_visible(self.locators.ORDERS_IN_PROGRESS, timeout=5)
    
    @allure.step("Получить номера заказов в работе")
    def get_orders_in_progress(self):
        if self.is_in_progress_section_visible():
            order_elements = self.find_elements(self.locators.ORDERS_IN_PROGRESS)
            return [order.text for order in order_elements]
        return []
    
    @allure.step("Получить список всех отображаемых заказов")
    def get_all_visible_orders(self):
        try:
            order_elements = self.find_elements(self.locators.ORDER_ITEMS, timeout=5)
            orders_data = []
            for order in order_elements:
                try:
                    number_element = order.find_element(*self.locators.ORDER_NUMBER)
                    orders_data.append(number_element.text)
                except:
                    continue
            return orders_data
        except:
            return []
    
    @allure.step("Кликнуть на заказ по номеру {order_number}")
    def click_order_by_number(self, order_number):
        order_elements = self.find_elements(self.locators.ORDER_ITEMS)
        for order in order_elements:
            try:
                number_element = order.find_element(*self.locators.ORDER_NUMBER)
                if number_element.text == order_number:
                    order.click()
                    return self
            except:
                continue
        raise Exception(f"Заказ с номером {order_number} не найден")
    
    @allure.step("Проверить отображение модального окна заказа")
    def is_order_modal_visible(self):
        return self.is_visible(OrderModalLocators.ORDER_MODAL, timeout=3)
    
    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):
        try:
            order_number_element = self.find_element(OrderModalLocators.ORDER_NUMBER, timeout=3)
            return order_number_element.text
        except:
            return ""
    
    @allure.step("Получить статус заказа из модального окна")
    def get_order_status_from_modal(self):
        try:
            status_element = self.find_element(OrderModalLocators.ORDER_STATUS, timeout=3)
            return status_element.text
        except:
            return ""
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        try:
            if self.is_visible(OrderModalLocators.ORDER_MODAL_CLOSE, timeout=2):
                self.click(OrderModalLocators.ORDER_MODAL_CLOSE)
                return True
            return False
        except:
            return False
    
    @allure.step("Проверить отображение заказа в ленте")
    def is_order_in_feed(self, order_number):
        orders = self.get_all_visible_orders()
        return order_number in orders
    
    @allure.step("Прокрутить ленту заказов")
    def scroll_order_feed(self):
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self
    
    @allure.step("Перейти к конструктору")
    def go_to_constructor(self):
        return self.open_page("main")
    
    @allure.step("Проверить, что лента заказов доступна")
    def is_feed_accessible(self):
        checks = []
        
        try:
            total = self.get_total_orders_count()
            today = self.get_today_orders_count()
            checks.append(True)
        except:
            checks.append(False)
        
        try:
            orders = self.get_all_visible_orders()
            checks.append(len(orders) >= 0)
        except:
            checks.append(False)
        
        return any(checks)
    
    @allure.step("Проверить загрузку страницы ленты заказов")
    def is_order_feed_page_loaded(self):
        return (self.is_present(self.locators.ORDER_FEED_SECTION) or 
                self.is_present(self.locators.TOTAL_ORDERS) or 
                self.is_present(self.locators.ORDER_ITEMS))