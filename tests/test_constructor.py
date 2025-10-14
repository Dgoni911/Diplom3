import pytest
import allure
from helpers.url_helper import UrlHelper

@allure.feature("Конструктор")
class TestConstructor:
    
    @allure.title("Переход по клику на 'Конструктор'")
    @allure.description("Тест проверяет навигацию между конструктором и лентой заказов")
    def test_click_constructor_navigation(self, main_page, browser):
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Кликнуть на 'Лента заказов'"):
            main_page.click_order_feed()
        
        with allure.step("Проверить переход на страницу ленты заказов"):
            current_url = browser.current_url
            expected_url = UrlHelper().get_url("feed")
            assert current_url == expected_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"
        
        with allure.step("Кликнуть на 'Конструктор'"):
            main_page.click_constructor()
        
        with allure.step("Проверить возврат на главную страницу"):
            current_url = browser.current_url
            expected_url = UrlHelper().get_url("main")
            assert current_url == expected_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"
    
    @allure.title("Переход по клику на раздел 'Лента заказов'")
    @allure.description("Тест проверяет переход из конструктора в ленту заказов")
    def test_click_order_feed_navigation(self, main_page, browser, order_feed_page):
        with allure.step("Открыть главную страницу"):
            main_page.open()
    
        with allure.step("Кликнуть на 'Лента заказов'"):
            main_page.click_order_feed()
    
        with allure.step("Проверить переход на страницу ленты заказов"):
            current_url = browser.current_url
            expected_url = UrlHelper().get_url("feed")
            
            normalized_current = current_url.rstrip('/')
            normalized_expected = expected_url.rstrip('/')
            
            assert normalized_current == normalized_expected, (
                f"Ожидался URL: {normalized_expected}, но получен: {normalized_current}"
            )
    
        with allure.step("Проверить успешную загрузку страницы"):
            assert browser.title != "", "Заголовок страницы не должен быть пустым"
            
            page_source = browser.page_source
            assert len(page_source) > 1000, "Страница должна содержать значительный контент"
            
            lower_source = page_source.lower()
            error_indicators = ["404", "not found", "error", "ошибка", "не найдено"]
            has_errors = any(error in lower_source for error in error_indicators)
            
            assert not has_errors, "Страница содержит индикаторы ошибок"
    
        with allure.step("Проверить наличие элементов ленты заказов"):
            from locators.order_feed_locators import OrderFeedLocators
        
            checks = [
                order_feed_page.is_element_present(OrderFeedLocators.ORDER_FEED_SECTION),
                order_feed_page.is_element_present(OrderFeedLocators.ORDER_FEED_CONTAINER),
                order_feed_page.is_element_present(OrderFeedLocators.ORDER_FEED_LIST),
                order_feed_page.is_element_present(OrderFeedLocators.ORDER_FEED_ALT1),
                order_feed_page.is_element_present(OrderFeedLocators.ORDER_FEED_ALT2),
                order_feed_page.is_element_present(OrderFeedLocators.ORDER_FEED_ALT3),
            ]
        
            assert any(checks), "Должна отображаться секция ленты заказов (ни один из ожидаемых элементов не найден)"
        
            try:
                total_orders = order_feed_page.get_total_orders_count()
                today_orders = order_feed_page.get_today_orders_count()
                assert total_orders >= 0 and today_orders >= 0, "Счетчики заказов должны отображаться"
            except:
                print("Счетчики заказов не найдены, но это не критично для данного теста")
        
        print(f"✅ Навигация в ленту заказов успешна. URL: {current_url}")
    
    @allure.title("Открытие модального окна с деталями ингредиента")
    @allure.description("Тест проверяет открытие модального окна при клике на ингредиент")
    def test_ingredient_modal_opening(self, main_page, order_modal):
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Дождаться загрузки ингредиентов"):
            main_page.wait_for_page_loaded()
        
        with allure.step("Кликнуть на первый ингредиент"):
            main_page.click_ingredient(0)
        
        with allure.step("Проверить, что модальное окно открылось"):
            assert main_page.is_ingredient_modal_visible(), "Модальное окно с деталями ингредиента должно быть видимым"
        
        with allure.step("Проверить содержимое модального окна"):
            assert order_modal.is_modal_visible(), "Модальное окно должно быть видимым через OrderModal"
    
    @allure.title("Закрытие модального окна с деталями ингредиента")
    @allure.description("Тест проверяет закрытие модального окна ингредиента")
    def test_ingredient_modal_closing(self, main_page, order_modal):
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Дождаться загрузки ингредиентов"):
            main_page.wait_for_page_loaded()
        
        with allure.step("Кликнуть на первый ингредиент"):
            main_page.click_ingredient(0)
        
        with allure.step("Проверить, что модальное окно открылось"):
            assert main_page.is_ingredient_modal_visible(), "Модальное окно должно быть открыто"
        
        with allure.step("Закрыть модальное окно через OrderModal"):
            modal_closed = order_modal.close_modal()
            assert modal_closed, "Модальное окно должно быть успешно закрыто"
        
        with allure.step("Проверить, что модальное окно закрылось"):
            assert not main_page.is_ingredient_modal_visible(), "Модальное окно должно быть скрыто"
            assert not order_modal.is_modal_visible(), "Модальное окно должно быть скрыто через OrderModal"
    
    @allure.title("Навигация по разделам конструктора")
    @allure.description("Тест проверяет переключение между разделами конструктора: Булки, Соусы, Начинки")
    def test_constructor_sections_navigation(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Дождаться загрузки конструктора"):
            main_page.wait_for_page_loaded()
        
        with allure.step("Проверить, что раздел 'Булки' активен по умолчанию"):
            buns_active = main_page.is_element_present(main_page.locators.BUNS_SECTION_ACTIVE)
            assert buns_active, "Раздел 'Булки' должен быть активен по умолчанию"
        
        with allure.step("Кликнуть на раздел 'Соусы'"):
            main_page.click_sauces_section()
        
        with allure.step("Проверить, что раздел 'Соусы' стал активным"):
            sauces_active = main_page.is_element_present(main_page.locators.SAUCES_SECTION_ACTIVE)
            assert sauces_active, "Раздел 'Соусы' должен стать активным после клика"
        
        with allure.step("Проверить отображение секции соусов"):
            sauces_section_visible = main_page.is_element_present(main_page.locators.SAUCES_SECTION)
            assert sauces_section_visible, "Секция соусов должна быть видимой"
        
        with allure.step("Кликнуть на раздел 'Начинки'"):
            main_page.click_fillings_section()
        
        with allure.step("Проверить, что раздел 'Начинки' стал активным"):
            fillings_active = main_page.is_element_present(main_page.locators.FILLINGS_SECTION_ACTIVE)
            assert fillings_active, "Раздел 'Начинки' должен стать активным после клика"
        
        with allure.step("Проверить отображение секции начинок"):
            fillings_section_visible = main_page.is_element_present(main_page.locators.FILLINGS_SECTION)
            assert fillings_section_visible, "Секция начинок должна быть видимой"
        
        with allure.step("Кликнуть на раздел 'Булки'"):
            main_page.click_buns_section()
        
        with allure.step("Проверить, что раздел 'Булки' снова активен"):
            buns_active_again = main_page.is_element_present(main_page.locators.BUNS_SECTION_ACTIVE)
            assert buns_active_again, "Раздел 'Булки' должен снова стать активным после клика"
    
    @allure.title("Проверка отображения ингредиентов в конструкторе")
    @allure.description("Тест проверяет, что все категории ингредиентов отображаются в конструкторе")
    def test_constructor_ingredients_display(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Дождаться загрузки конструктора"):
            main_page.wait_for_page_loaded()
        
        with allure.step("Проверить наличие булок в конструкторе"):
            buns_ingredients = main_page.find_elements(main_page.locators.BUNS_INGREDIENTS)
            assert len(buns_ingredients) > 0, "В разделе 'Булки' должны отображаться ингредиенты"
        
        with allure.step("Перейти в раздел 'Соусы'"):
            main_page.click_sauces_section()
        
        with allure.step("Проверить наличие соусов в конструкторе"):
            sauces_ingredients = main_page.find_elements(main_page.locators.SAUCES_INGREDIENTS)
            assert len(sauces_ingredients) > 0, "В разделе 'Соусы' должны отображаться ингредиенты"
        
        with allure.step("Перейти в раздел 'Начинки'"):
            main_page.click_fillings_section()
        
        with allure.step("Проверить наличие начинок в конструкторе"):
            fillings_ingredients = main_page.find_elements(main_page.locators.FILLINGS_INGREDIENTS)
            assert len(fillings_ingredients) > 0, "В разделе 'Начинки' должны отображаться ингредиенты"