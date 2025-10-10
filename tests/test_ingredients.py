import pytest
import allure


@allure.epic("Stellar Burgers UI")
@allure.feature("Работа с ингредиентами")
class TestIngredients:
    
    @allure.title("Добавление булки в конструктор")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.constructor
    def test_add_bun_to_constructor(self, main_page):
        from locators.constructor_locators import ConstructorLocators
        
        main_page.add_ingredient_to_constructor(ConstructorLocators.BUN_INGREDIENT)
        
        assert main_page.is_element_present(ConstructorLocators.BUN_DROP_ZONE), "Булка не добавлена в конструктор"
    
    @allure.title("Добавление соуса в конструктор")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.constructor
    def test_add_sauce_to_constructor(self, main_page):
        from locators.constructor_locators import ConstructorLocators
        
        main_page.add_ingredient_to_constructor(ConstructorLocators.SAUCE_INGREDIENT)
        
        ingredient_element = main_page.get_ingredient_element(5)  
        counter = main_page.get_ingredient_counter(ingredient_element)
        
        assert counter > 0, "Счетчик соуса не увеличился после добавления"
    
    @allure.title("Добавление начинки в конструктор")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.constructor
    def test_add_filling_to_constructor(self, main_page):
        from locators.constructor_locators import ConstructorLocators
        
        main_page.add_ingredient_to_constructor(ConstructorLocators.FILLING_INGREDIENT)
        
        ingredient_element = main_page.get_ingredient_element(10)  
        counter = main_page.get_ingredient_counter(ingredient_element)
        
        assert counter > 0, "Счетчик начинки не увеличился после добавления"