import pytest
import allure

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Увеличение счетчика 'Выполнено за всё время'")
    @pytest.mark.skip(reason="Order creation functionality needs implementation")
    def test_total_orders_counter_increase(self, order_feed_page):
        initial_total = order_feed_page.get_total_orders_count()
        order_feed_page.open()
        new_total = order_feed_page.get_total_orders_count()
        assert new_total > initial_total
    
    @allure.title("Увеличение счетчика 'Выполнено за сегодня'")
    @pytest.mark.skip(reason="Order creation functionality needs implementation")
    def test_today_orders_counter_increase(self, order_feed_page):
        initial_today = order_feed_page.get_today_orders_count()
        order_feed_page.open()
        new_today = order_feed_page.get_today_orders_count()
        assert new_today > initial_today
    
    @allure.title("Появление номера заказа в разделе 'В работе'")
    @pytest.mark.skip(reason="Order creation and tracking functionality needs implementation")
    def test_order_appears_in_progress(self, order_feed_page):
        order_number = "12345"
        orders_in_progress = order_feed_page.get_orders_in_progress()
        assert order_number in orders_in_progress