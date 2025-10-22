import pytest
import allure
from helpers.url_helper import UrlHelper

@allure.feature("Конструктор")
class TestConstructor:
    
    @allure.title("Переход по клику на 'Конструктор'")
    @allure.description("Тест проверяет навигацию между конструктором и лентой заказов")
    def test_click_constructor_navigation(self, main_page):
        with allure.step("Перейти на страницу ленты заказов"):
            main_page.click_order_feed()
        
        with allure.step("Проверить переход на страницу ленты заказов"):
            current_url = main_page.get_current_url()
            assert "feed" in current_url, f"Должны находиться на странице ленты заказов, но URL: {current_url}"
        
        with allure.step("Кликнуть на 'Конструктор'"):
            main_page.click_constructor()
        
        with allure.step("Проверить возврат на главную страницу"):
            assert main_page.is_main_page_loaded(), "Должны вернуться на главную страницу"
    
    @allure.title("Переход по клику на раздел 'Лента заказов'")
    @allure.description("Тест проверяет переход из конструктора в ленту заказов")
    def test_click_order_feed_navigation(self, main_page):
        with allure.step("Кликнуть на 'Лента заказов'"):
            main_page.click_order_feed()
    
        with allure.step("Проверить переход на страницу ленты заказов"):
            current_url = main_page.get_current_url()
            assert "feed" in current_url, f"Должны находиться на странице ленты заказов, но URL: {current_url}"
    
    @allure.title("Открытие модального окна с деталями ингредиента")
    @allure.description("Тест проверяет открытие модального окна при клике на ингредиент")
    def test_ingredient_modal_opening(self, main_page):
        with allure.step("Кликнуть на первый ингредиент"):
            main_page.click_ingredient(0)
        
        with allure.step("Проверить, что модальное окно открылось"):
            assert main_page.is_ingredient_modal_visible(), "Модальное окно с деталями ингредиента должно быть видимым"
    
    @allure.title("Закрытие модального окна с деталями ингредиента")
    @allure.description("Тест проверяет закрытие модального окна ингредиента")
    def test_ingredient_modal_closing(self, main_page, order_modal):
        with allure.step("Кликнуть на первый ингредиент"):
            main_page.click_ingredient(0)

        with allure.step("Проверить, что модальное окно открылось"):
            assert main_page.is_ingredient_modal_visible(), "Модальное окно должно быть открыто"
            assert order_modal.is_modal_visible(), "Модальное окно должно быть видимо через OrderModal"

        with allure.step("Закрыть модальное окно через OrderModal"):
            modal_closed = order_modal.close_modal()
        
            if not modal_closed:
                modal_closed = order_modal.force_close_modal()
        
            assert modal_closed, "Модальное окно должно быть успешно закрыто"

        with allure.step("Проверить, что модальное окно закрылось"):
            main_page_closed = not main_page.is_ingredient_modal_visible()
            order_modal_closed = not order_modal.is_modal_visible()
        
            assert main_page_closed or order_modal_closed, "Модальное окно должно быть скрыто"
        
            assert main_page.is_constructor_button_present(), "После закрытия модального окна должны видеть элементы главной страницы"
    
    @allure.title("Навигация по разделам конструктора")
    @allure.description("Тест проверяет переключение между разделами конструктора: Булки, Соусы, Начинки")
    def test_constructor_sections_navigation(self, main_page):
        with allure.step("Проверить, что раздел 'Булки' активен по умолчанию"):
            assert main_page.is_buns_section_active(), "Раздел 'Булки' должен быть активен по умолчанию"
        
        with allure.step("Кликнуть на раздел 'Соусы'"):
            main_page.click_sauces_section()
        
        with allure.step("Проверить, что раздел 'Соусы' стал активным"):
            assert main_page.is_sauces_section_active(), "Раздел 'Соусы' должен стать активным после клика"
        
        with allure.step("Кликнуть на раздел 'Начинки'"):
            main_page.click_fillings_section()
        
        with allure.step("Проверить, что раздел 'Начинки' стал активным"):
            assert main_page.is_fillings_section_active(), "Раздел 'Начинки' должен стать активным после клика"
        
        with allure.step("Кликнуть на раздел 'Булки'"):
            main_page.click_buns_section()
        
        with allure.step("Проверить, что раздел 'Булки' снова активен"):
            assert main_page.is_buns_section_active(), "Раздел 'Булки' должен снова стать активным после клика"
    
    @allure.title("Проверка отображения ингредиентов в конструкторе")
    @allure.description("Тест проверяет, что все категории ингредиентов отображаются в конструкторе")
    def test_constructor_ingredients_display(self, main_page):
        with allure.step("Проверить наличие булок в конструкторе"):
            assert main_page.has_buns_ingredients(), "В разделе 'Булки' должны отображаться ингредиенты"
        
        with allure.step("Перейти в раздел 'Соусы'"):
            main_page.click_sauces_section()
        
        with allure.step("Проверить наличие соусов в конструкторе"):
            assert main_page.has_sauces_ingredients(), "В разделе 'Соусы' должны отображаться ингредиенты"
        
        with allure.step("Перейти в раздел 'Начинки'"):
            main_page.click_fillings_section()
        
        with allure.step("Проверить наличие начинок в конструкторе"):
            assert main_page.has_fillings_ingredients(), "В разделе 'Начинки' должны отображаться ингредиенты"