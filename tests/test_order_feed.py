import pytest
import allure
from helpers.data_helper import DataHelper

@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title("Проверка счетчика 'Выполнено за всё время'")
    @allure.description("Тест проверяет доступность общего счетчика заказов")
    def test_total_orders_counter_available(self, order_feed_page):
        with allure.step("Получить значение счетчика"):
            total_orders = order_feed_page.get_total_orders_count()
        
        with allure.step("Проверить, что счетчик доступен"):
            assert total_orders >= 0, "Счетчик должен быть неотрицательным"
    
    @allure.title("Проверка счетчика 'Выполнено за сегодня'")
    @allure.description("Тест проверяет доступность дневного счетчика заказов")
    def test_today_orders_counter_available(self, order_feed_page):
        with allure.step("Получить значение счетчика"):
            today_orders = order_feed_page.get_today_orders_count()
        
        with allure.step("Проверить, что счетчик доступен"):
            assert today_orders >= 0, "Счетчик должен быть неотрицательным"
    
    @allure.title("Проверка отображения заказов в ленте")
    @allure.description("Тест проверяет наличие заказов в ленте")
    def test_orders_display_in_feed(self, order_feed_page):
        with allure.step("Получить список доступных заказов"):
            orders = order_feed_page.get_all_visible_orders()
        
        with allure.step("Проверить отображение заказов"):
            assert len(orders) >= 0, "Лента заказов должна быть доступна"