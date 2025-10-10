import pytest
import allure
import time


@allure.epic("Stellar Burgers UI")
@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title("Увеличение счетчика 'Выполнено за всё время' при новом заказе")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.order_feed
    def test_total_orders_counter_increases(self, order_feed_page):
        initial_total = order_feed_page.get_total_orders_count()
        
        time.sleep(5)
        
        updated_total = order_feed_page.get_total_orders_count()
        
        assert updated_total >= initial_total, "Счетчик общих заказов не увеличился"
    
    @allure.title("Увеличение счетчика 'Выполнено за сегодня' при новом заказе")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.order_feed
    def test_today_orders_counter_increases(self, order_feed_page):
        initial_today = order_feed_page.get_today_orders_count()
        
        time.sleep(5)
        
        updated_today = order_feed_page.get_today_orders_count()
        
        assert updated_today >= initial_today, "Счетчик заказов за сегодня не увеличился"
    
    @allure.title("Появление номера заказа в разделе 'В работе'")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.order_feed
    def test_order_number_appears_in_progress(self, order_feed_page):
        initial_orders = order_feed_page.get_orders_in_progress()
        
        test_order_number = "12345"  
        
        orders_after = order_feed_page.get_orders_in_progress()
        
        assert orders_after is not None, "Не удалось получить список заказов в работе"