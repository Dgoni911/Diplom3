import allure
from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    
    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        count_text = self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNT)
        return int(count_text)
    
    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        count_text = self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNT)
        return int(count_text)
    
    @allure.step("Получить номера заказов в работе")
    def get_orders_in_progress(self):
        orders = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        order_numbers = []
        for order in orders:
            try:
                number = order.find_element(*OrderFeedLocators.ORDER_NUMBER).text
                order_numbers.append(number)
            except:
                continue
        return order_numbers
    
    @allure.step("Проверить наличие номера заказа в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        orders_in_progress = self.get_orders_in_progress()
        return order_number in orders_in_progress
    
    @allure.step("Подождать обновления счетчиков")
    def wait_for_counters_update(self, initial_total, initial_today, timeout=30):
        import time
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            current_total = self.get_total_orders_count()
            current_today = self.get_today_orders_count()
            
            if current_total > initial_total or current_today > initial_today:
                return True
            
            time.sleep(1)
        
        return False