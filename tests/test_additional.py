import pytest
import allure
from helpers.url_helper import UrlHelper

@allure.feature("Дополнительные тесты")
class TestAdditional:
    
    @allure.title("Проверка заголовка страницы")
    @allure.description("Тест проверяет корректность заголовка главной страницы")
    def test_page_title(self, main_page, browser):
        with allure.step("Открыть главную страницу"):
            main_page.open()
    
        with allure.step("Дождаться полной загрузки страницы"):
            main_page.wait_for_page_loaded()
    
        with allure.step("Получить заголовок страницы"):
            page_title = browser.title
    
        with allure.step("Проверить, что заголовок содержит 'Stellar Burgers'"):
            assert "Stellar" in page_title or "Бургеры" in page_title, f"Заголовок страницы должен содержать 'Stellar' или 'Бургеры', но получен: {page_title}"
    
    @allure.title("Проверка наличия основных элементов на главной странице")
    @allure.description("Тест проверяет наличие всех ключевых элементов интерфейса на главной странице")
    def test_main_page_elements(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Дождаться полной загрузки страницы"):
            main_page.wait_for_page_loaded()
        
        with allure.step("Проверить наличие кнопки конструктора"):
            constructor_present = main_page.is_element_present(main_page.locators.CONSTRUCTOR_BUTTON)
            assert constructor_present, "Кнопка конструктора должна присутствовать на главной странице"
        
        with allure.step("Проверить наличие кнопки ленты заказов"):
            order_feed_present = main_page.is_element_present(main_page.locators.ORDER_FEED_BUTTON)
            assert order_feed_present, "Кнопка ленты заказов должна присутствовать на главной странице"
        
        with allure.step("Проверить наличие кнопки личного кабинета"):
            personal_account_present = main_page.is_element_present(main_page.locators.PERSONAL_ACCOUNT_BUTTON)
            assert personal_account_present, "Кнопка личного кабинета должна присутствовать на главной странице"
        
        with allure.step("Проверить наличие секции с ингредиентами"):
            ingredients_section_present = main_page.is_element_present(main_page.locators.INGREDIENTS_SECTION)
            assert ingredients_section_present, "Секция с ингредиентами должна присутствовать на главной странице"
        
        with allure.step("Получить список всех ингредиентов"):
            ingredients = main_page.find_elements(main_page.locators.INGREDIENT_ITEM)
        
        with allure.step("Проверить, что ингредиенты отображаются"):
            assert len(ingredients) > 0, "На главной странице должны отображаться ингредиенты для конструктора бургеров"
    
    @allure.title("Проверка перехода в личный кабинет без авторизации")
    @allure.description("Тест проверяет редирект на страницу логина при попытке доступа к личному кабинету без авторизации")
    def test_personal_account_redirect(self, main_page, browser):
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Дождаться полной загрузки страницы"):
            main_page.wait_for_page_loaded()
        
        with allure.step("Кликнуть на кнопку 'Личный кабинет'"):
            main_page.click_personal_account()
        
        with allure.step("Дождаться загрузки страницы логина"):
            main_page.wait_for_element_visible(main_page.locators.LOGIN_BUTTON, timeout=5)
        
        with allure.step("Получить текущий URL страницы"):
            current_url = browser.current_url
        
        with allure.step("Проверить, что произошел редирект на страницу логина"):
            assert "login" in current_url, f"Ожидался переход на страницу логина, но текущий URL: {current_url}"
        
        with allure.step("Проверить наличие формы логина"):
            login_form_present = main_page.is_element_present(main_page.locators.LOGIN_FORM)
            assert login_form_present, "На странице должна отображаться форма логина"
    
    @allure.title("Проверка логотипа и его кликабельности")
    @allure.description("Тест проверяет наличие логотипа и его функциональность - возврат на главную страницу")
    def test_logo_clickable(self, main_page, browser):
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Дождаться полной загрузки страницы"):
            main_page.wait_for_page_loaded()
        
        with allure.step("Проверить наличие логотипа на странице"):
            logo_present = main_page.is_element_present(main_page.locators.LOGO)
            assert logo_present, "Логотип должен присутствовать на главной странице"
        
        with allure.step("Перейти на страницу ленты заказов"):
            main_page.click_order_feed()
        
        with allure.step("Дождаться загрузки ленты заказов"):
            main_page.wait_for_page_loaded()
        
        with allure.step("Проверить, что текущая страница - лента заказов"):
            current_url_before_click = browser.current_url
            assert "feed" in current_url_before_click, "Должны находиться на странице ленты заказов"
        
        with allure.step("Кликнуть на логотип"):
            main_page.click_element(main_page.locators.LOGO)
        
        with allure.step("Дождаться загрузки главной страницы"):
            main_page.wait_for_page_loaded()
        
        with allure.step("Получить текущий URL после клика на логотип"):
            current_url_after_click = browser.current_url
        
        with allure.step("Проверить, что произошел возврат на главную страницу"):
            expected_url = UrlHelper().get_url("main")
            assert current_url_after_click == expected_url, f"Клик по логотипу должен возвращать на главную страницу. Ожидалось: {expected_url}, получено: {current_url_after_click}"
    
    @allure.title("Проверка навигационного меню")
    @allure.description("Тест проверяет функциональность навигационного меню и переключение между разделами")
    def test_navigation_menu(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Дождаться полной загрузки страницы"):
            main_page.wait_for_page_loaded()
        
        with allure.step("Проверить, что конструктор активен по умолчанию"):
            is_constructor_active = main_page.is_element_present(main_page.locators.CONSTRUCTOR_ACTIVE)
            assert is_constructor_active, "Раздел конструктора должен быть активен по умолчанию"
        
        with allure.step("Кликнуть на кнопку ленты заказов"):
            main_page.click_order_feed()
        
        with allure.step("Проверить, что лента заказов стала активной"):
            is_order_feed_active = main_page.is_element_present(main_page.locators.ORDER_FEED_ACTIVE)
            assert is_order_feed_active, "Раздел ленты заказов должен стать активным после клика"
        
        with allure.step("Вернуться в конструктор"):
            main_page.click_constructor()
        
        with allure.step("Проверить, что конструктор снова активен"):
            is_constructor_active_again = main_page.is_element_present(main_page.locators.CONSTRUCTOR_ACTIVE)
            assert is_constructor_active_again, "Раздел конструктора должен снова стать активным после клика"