import pytest
import allure
from helpers.url_helper import UrlHelper

@allure.feature("Дополнительные тесты")
class TestAdditional:
    
    @allure.title("Проверка заголовка страницы")
    @allure.description("Тест проверяет корректность заголовка главной страницы")
    def test_page_title(self, main_page):
        with allure.step("Получить заголовок страницы"):
            page_title = main_page.get_page_title()
    
        with allure.step("Проверить, что заголовок содержит 'Stellar Burgers'"):
            assert "Stellar" in page_title or "Бургеры" in page_title, f"Заголовок страницы должен содержать 'Stellar' или 'Бургеры', но получен: {page_title}"
    
    @allure.title("Проверка наличия основных элементов на главной странице")
    @allure.description("Тест проверяет наличие всех ключевых элементов интерфейса на главной странице")
    def test_main_page_elements(self, main_page):
        with allure.step("Проверить наличие кнопки конструктора"):
            assert main_page.is_constructor_button_present(), "Кнопка конструктора должна присутствовать на главной странице"
        
        with allure.step("Проверить наличие кнопки ленты заказов"):
            assert main_page.is_order_feed_button_present(), "Кнопка ленты заказов должна присутствовать на главной странице"
        
        with allure.step("Проверить наличие кнопки личного кабинета"):
            assert main_page.is_personal_account_button_present(), "Кнопка личного кабинета должна присутствовать на главной странице"
        
        with allure.step("Проверить наличие секции с ингредиентами"):
            assert main_page.is_ingredients_section_present(), "Секция с ингредиентами должна присутствовать на главной странице"
        
        with allure.step("Проверить, что ингредиенты отображаются"):
            assert main_page.has_ingredients(), "На главной странице должны отображаться ингредиенты для конструктора бургеров"
    
    @allure.title("Проверка перехода в личный кабинет без авторизации")
    @allure.description("Тест проверяет редирект на страницу логина при попытке доступа к личному кабинету без авторизации")
    def test_personal_account_redirect(self, main_page, login_page):
        with allure.step("Кликнуть на кнопку 'Личный кабинет'"):
            main_page.click_personal_account()
        
        with allure.step("Проверить, что произошел редирект на страницу логина"):
            current_url = main_page.get_current_url()
            assert "login" in current_url, f"Ожидался переход на страницу логина, но текущий URL: {current_url}"
    
    @allure.title("Проверка логотипа и его кликабельности")
    @allure.description("Тест проверяет наличие логотипа и его функциональность - возврат на главную страницу")
    def test_logo_clickable(self, main_page):
        with allure.step("Проверить наличие логотипа на странице"):
            assert main_page.is_logo_present(), "Логотип должен присутствовать на главной странице"
        
        with allure.step("Перейти на страницу ленты заказов"):
            main_page.click_order_feed()
        
        with allure.step("Проверить, что текущая страница - лента заказов"):
            current_url = main_page.get_current_url()
            assert "feed" in current_url, f"Должны находиться на странице ленты заказов, но URL: {current_url}"
        
        with allure.step("Кликнуть на логотип"):
            main_page.click_logo()
        
        with allure.step("Проверить, что произошел возврат на главную страницу"):
            assert main_page.is_main_page_loaded(), "Клик по логотипу должен возвращать на главную страницу"
    
    @allure.title("Проверка навигационного меню")
    @allure.description("Тест проверяет функциональность навигационного меню и переключение между разделами")
    def test_navigation_menu(self, main_page):
        with allure.step("Проверить, что конструктор активен по умолчанию"):
            assert main_page.is_constructor_active(), "Раздел конструктора должен быть активен по умолчанию"
        
        with allure.step("Кликнуть на кнопку ленты заказов"):
            main_page.click_order_feed()
        
        with allure.step("Проверить, что лента заказов стала активной"):
            assert main_page.is_order_feed_active(), "Раздел ленты заказов должен стать активным после клика"
        
        with allure.step("Вернуться в конструктор"):
            main_page.click_constructor()
        
        with allure.step("Проверить, что конструктор снова активен"):
            assert main_page.is_constructor_active(), "Раздел конструктора должен снова стать активным после клика"