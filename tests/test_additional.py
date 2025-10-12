import pytest
import allure
from helpers.url_helper import UrlHelper

@allure.feature("Дополнительные тесты")
class TestAdditional:
    @allure.title("Проверка заголовка страницы")
    def test_page_title(self, main_page, browser):
        with allure.step("Проверяем заголовок страницы"):
            assert "Stellar Burgers" in browser.title
    
    @allure.title("Проверка наличия основных элементов на главной странице")
    def test_main_page_elements(self, main_page):
        with allure.step("Проверяем наличие кнопки конструктора"):
            assert main_page.is_element_present(main_page.locators.CONSTRUCTOR_BUTTON)
        
        with allure.step("Проверяем наличие кнопки ленты заказов"):
            assert main_page.is_element_present(main_page.locators.ORDER_FEED_BUTTON)
        
        with allure.step("Проверяем наличие ингредиентов"):
            ingredients = main_page.find_elements(main_page.locators.INGREDIENT_ITEM)
            assert len(ingredients) > 0, "Должны быть отображены ингредиенты"
    
    @allure.title("Проверка перехода в личный кабинет без авторизации")
    def test_personal_account_redirect(self, main_page, browser):
        with allure.step("Кликаем на 'Личный кабинет'"):
            main_page.click_personal_account()
        
        with allure.step("Проверяем редирект на страницу логина"):
            main_page.wait_for_element_visible(main_page.locators.LOGIN_BUTTON, timeout=5)
            assert "login" in browser.current_url, f"Ожидался переход на страницу логина, но текущий URL: {browser.current_url}"
    
    @allure.title("Проверка логотипа и его кликабельности")
    def test_logo_clickable(self, main_page, browser):
        with allure.step("Проверяем наличие логотипа"):
            assert main_page.is_element_present(main_page.locators.LOGO), "Логотип должен присутствовать на странице"
        
        with allure.step("Кликаем на логотип"):
            main_page.click_element(main_page.locators.LOGO)
        
        with allure.step("Проверяем, что остались на главной странице"):
            assert browser.current_url == UrlHelper.get_url("main"), "Клик по логотипу должен оставлять на главной странице"