import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Stellar Burgers UI")
@allure.feature("Конструктор бургеров")
class TestConstructor:
    
    @allure.title("Переход по клику на 'Конструктор'")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.constructor
    def test_click_constructor_navigation(self, main_page):
        main_page.click_order_feed()
        main_page.click_constructor()
        
        assert main_page.is_constructor_active(), "Раздел конструктора не активен после клика"
    
    @allure.title("Переход по клику на 'Лента заказов'")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.constructor
    def test_click_order_feed_navigation(self, main_page):
        main_page.click_order_feed()
        
        assert main_page.is_order_feed_active(), "Раздел ленты заказов не активен после клика"
    
    @allure.title("Открытие деталей ингредиента по клику")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    @pytest.mark.constructor
    def test_ingredient_click_opens_modal(self, main_page):
        main_page.click_ingredient(0)
        
        assert main_page.is_modal_visible(), "Окно с деталями ингредиента не открылось"
        
        details_text = main_page.get_ingredient_details_text()
        assert details_text, "Текст деталей ингредиента пустой"
    
    @allure.title("Закрытие окна по крестику")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    @pytest.mark.constructor
    def test_modal_close_by_button(self, main_page):
        main_page.click_ingredient(0)
        main_page.wait_for_element_visible(main_page.locators.MODAL)
        
        main_page.close_modal()
        main_page.wait_for_element_invisible(main_page.locators.MODAL)
        
        assert not main_page.is_modal_visible(), "Окно не закрылось"
    
    @allure.title("Увеличение счетчика ингредиента при добавлении")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.constructor
    def test_ingredient_counter_increases_on_add(self, main_page):
        from locators.constructor_locators import ConstructorLocators
        
        ingredient_element = main_page.get_ingredient_element(0)
        initial_counter = main_page.get_ingredient_counter(ingredient_element)
        
        main_page.add_ingredient_to_constructor(ConstructorLocators.BUN_INGREDIENT)
        
        updated_counter = main_page.get_ingredient_counter(ingredient_element)
        
        assert updated_counter > initial_counter, f"Счетчик не увеличился: было {initial_counter}, стало {updated_counter}"