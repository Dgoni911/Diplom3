import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.constructor_locators import ConstructorLocators


class MainPage(BasePage):
    
    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait.wait_for_page_load()
    
    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait.wait_for_page_load()
    
    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self, index=0):
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            self.browser.scroll_to_element(ingredients[index])
            self.click_by_element(ingredients[index])
    
    @allure.step("Кликнуть на элемент напрямую")
    def click_by_element(self, element):
        self.browser.safe_click_element(element)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait.wait_for_element_to_disappear(MainPageLocators.MODAL)
    
    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_locator):
        self.drag_and_drop(ingredient_locator, ConstructorLocators.INGREDIENTS_DROP_ZONE)
        
        self.wait.wait_for_condition(
            lambda: self.get_ingredient_counter(self.get_ingredient_element(0)) > 0,
            timeout=10,
            description="Счетчик ингредиента не обновился"
        )