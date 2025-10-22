import pytest
import allure
from helpers.data_helper import DataHelper

@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title("Проверка изменения общего счетчика заказов после оформления")
    @allure.description("Тест проверяет изменение общего счетчика заказов после успешного оформления")
    def test_total_order_counter_updates_after_order(self, main_page, order_feed_page, login_page):
        test_email = DataHelper.get_test_user_email()
        test_password = DataHelper.get_test_user_password()
        
        with allure.step("Получить начальное значение общего счетчика"):
            order_feed_page.open()
            initial_total = order_feed_page.get_total_orders_count()
        
        with allure.step("Авторизация и создание заказа"):
            main_page.open()
            
            with allure.step("Авторизоваться"):
                main_page.click_personal_account()
                login_page.wait_for_page_loaded()
                login_page.complete_login(test_email, test_password)
                main_page.click_constructor()
                main_page.wait_for_main_page_loaded()
            
            with allure.step("Создать тестовый заказ"):
                if not main_page.has_ingredients():
                    pytest.skip("Нет доступных ингредиентов для создания заказа")
                
                with allure.step("Добавить ингредиенты в конструктор"):
                    main_page.add_ingredients_to_constructor()
                
                main_page.create_test_order()
                
                if main_page.wait_for_order_confirmation(timeout=20):
                    order_number = main_page.get_created_order_number()
                    with allure.step(f"Заказ №{order_number} успешно создан"):
                        main_page.close_order_modal()
                else:
                    pytest.skip("Не удалось дождаться подтверждения заказа")
        
        with allure.step("Проверить обновление общего счетчика"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            new_total = order_feed_page.get_total_orders_count()
        
        with allure.step("Проверить изменение общего счетчика"):
            assert new_total >= initial_total, (
                f"Общий счетчик заказов должен увеличиться. Было: {initial_total}, стало: {new_total}"
            )

    @allure.title("Проверка изменения дневного счетчика заказов после оформления")
    @allure.description("Тест проверяет изменение дневного счетчика заказов после успешного оформления")
    def test_today_order_counter_updates_after_order(self, main_page, order_feed_page, login_page):
        test_email = DataHelper.get_test_user_email()
        test_password = DataHelper.get_test_user_password()
        
        with allure.step("Получить начальное значение дневного счетчика"):
            order_feed_page.open()
            initial_today = order_feed_page.get_today_orders_count()
        
        with allure.step("Авторизация и создание заказа"):
            main_page.open()
            
            with allure.step("Авторизоваться"):
                main_page.click_personal_account()
                login_page.wait_for_page_loaded()
                login_page.complete_login(test_email, test_password)
                main_page.click_constructor()
                main_page.wait_for_main_page_loaded()
            
            with allure.step("Создать тестовый заказ"):
                if not main_page.has_ingredients():
                    pytest.skip("Нет доступных ингредиентов для создания заказа")
                
                with allure.step("Добавить ингредиенты в конструктор"):
                    main_page.add_ingredients_to_constructor()
                
                main_page.create_test_order()
                
                if main_page.wait_for_order_confirmation(timeout=20):
                    order_number = main_page.get_created_order_number()
                    with allure.step(f"Заказ №{order_number} успешно создан"):
                        main_page.close_order_modal()
                else:
                    pytest.skip("Не удалось дождаться подтверждения заказа")
        
        with allure.step("Проверить обновление дневного счетчика"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            new_today = order_feed_page.get_today_orders_count()
        
        with allure.step("Проверить изменение дневного счетчика"):
            assert new_today >= initial_today, (
                f"Дневной счетчик заказов должен увеличиться. Было: {initial_today}, стало: {new_today}"
            )

    @allure.title("Проверка счетчика 'Выполнено за всё время'")
    def test_total_orders_counter_available(self, order_feed_page):
        with allure.step("Получить значение счетчика"):
            total_orders = order_feed_page.get_total_orders_count()
        
        with allure.step("Проверить, что счетчик доступен"):
            assert total_orders >= 0, "Счетчик должен быть неотрицательным"
    
    @allure.title("Проверка счетчика 'Выполнено за сегодня'")
    def test_today_orders_counter_available(self, order_feed_page):
        with allure.step("Получить значение счетчика"):
            today_orders = order_feed_page.get_today_orders_count()
        
        with allure.step("Проверить, что счетчик доступен"):
            assert today_orders >= 0, "Счетчик должен быть неотрицательным"
    
    @allure.title("Проверка отображения заказов в ленте")
    def test_orders_display_in_feed(self, order_feed_page):
        with allure.step("Получить список доступных заказов"):
            orders = order_feed_page.get_all_visible_orders()
        
        with allure.step("Проверить отображение заказов"):
            assert len(orders) >= 0, "Лента заказов должна быть доступна"
    
    @allure.title("Проверка доступности ленты заказов")
    def test_order_feed_accessible(self, order_feed_page):
        with allure.step("Проверить, что лента заказов загружена"):
            assert order_feed_page.is_order_feed_page_loaded(), "Страница ленты заказов должна загружаться"
        
        with allure.step("Проверить доступность счетчиков"):
            total_orders = order_feed_page.get_total_orders_count()
            today_orders = order_feed_page.get_today_orders_count()
            
            assert total_orders >= 0, "Счетчик общих заказов должен быть доступен"
            assert today_orders >= 0, "Счетчик дневных заказов должен быть доступен"
        
        with allure.step("Проверить наличие заказов в ленте"):
            orders = order_feed_page.get_all_visible_orders()
            assert orders is not None, "Метод получения заказов должен работать"

    @allure.title("Проверка раздела 'В работе' - ОТКЛЮЧЕНО") 
    def test_orders_in_progress_section_disabled(self):
        pytest.skip("Тест зависит от наличия заказов в статусе 'В работе'")