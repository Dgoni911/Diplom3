import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_modal_locators import OrderModalLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
    
    @allure.step("Открыть главную страницу")
    def open(self):
        return self.open_page("main")
    
    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_main_page_loaded(self):
        self.wait_for_page_loaded()
        
        possible_elements = [
            self.locators.CONSTRUCTOR_BUTTON,
            self.locators.INGREDIENTS_SECTION,
            self.locators.ORDER_BUTTON,
            self.locators.PAGE_TITLE,
            self.locators.CONSTRUCTOR_TEXT,
        ]
        
        for element in possible_elements:
            if self.is_present(element, timeout=3):
                return True
        
        self.take_screenshot("page_loaded_failed")
        raise Exception("Не удалось дождаться загрузки главной страницы")
    
    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        self.click(self.locators.CONSTRUCTOR_BUTTON_ALT)
        return self
    
    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        self.click(self.locators.ORDER_FEED_BUTTON_ALT)
        return self.wait_for_page_loaded()
    
    @allure.step("Кликнуть на личный кабинет")
    def click_personal_account(self):
        self.click(self.locators.PERSONAL_ACCOUNT_BUTTON_ALT)
        return self.wait_for_page_loaded()
    
    @allure.step("Кликнуть на ингредиент {index}")
    def click_ingredient(self, index=0):
        all_ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        
        if all_ingredients and index < len(all_ingredients):
            self.execute_script("arguments[0].scrollIntoView(true);", all_ingredients[index])
            all_ingredients[index].click()
            self.wait.wait_for_element_visible(OrderModalLocators.INGREDIENT_DETAILS)
        return self
    
    @allure.step("Проверить видимость модального окна ингредиента")
    def is_ingredient_modal_visible(self):
        return self.is_visible(OrderModalLocators.INGREDIENT_DETAILS, timeout=3)
    
    @allure.step("Кликнуть 'Сделать заказ'")
    def click_make_order(self):
        self.click(self.locators.ORDER_BUTTON)
        return self
    
    @allure.step("Кликнуть на раздел булок")
    def click_buns_section(self):
        self.click(self.locators.BUNS_SECTION)
        return self
    
    @allure.step("Кликнуть на раздел соусов")
    def click_sauces_section(self):
        self.click(self.locators.SAUCES_SECTION)
        return self
    
    @allure.step("Кликнуть на раздел начинок")
    def click_fillings_section(self):
        self.click(self.locators.FILLINGS_SECTION)
        return self
    
    @allure.step("Добавить ингредиент в конструктор по индексу {index}")
    def add_ingredient_to_constructor(self, index):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if not ingredients or index >= len(ingredients):
            raise Exception(f"Ингредиент с индексом {index} не найден")
        
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", ingredients[index])
        
        self.wait.wait_for_element_visible(self.locators.INGREDIENT_ITEM)
        
        constructor_area = self.find_element(self.locators.CONSTRUCTOR_AREA)
        
        action = ActionChains(self.driver)
        action.drag_and_drop(ingredients[index], constructor_area).perform()
        
        return self

    @allure.step("Добавить ингредиенты в конструктор")
    def add_ingredients_to_constructor(self):
        """Добавляет базовые ингредиенты в конструктор"""
        with allure.step("Добавить булку"):
            self.add_ingredient_to_constructor(0)
        
        with allure.step("Добавить соус"):
            sauces_start_index = 2  
            self.add_ingredient_to_constructor(sauces_start_index)
        
        with allure.step("Добавить начинку"):
            fillings_start_index = 4  
            self.add_ingredient_to_constructor(fillings_start_index)
        
        return self

    @allure.step("Создать тестовый заказ")
    def create_test_order(self):
        self.wait.wait_for_element_visible(self.locators.INGREDIENT_ITEM)
    
        self.add_ingredients_to_constructor()
    
        if not self.is_visible(self.locators.ORDER_BUTTON_ACTIVE, timeout=5):
            raise Exception("Кнопка 'Оформить заказ' не стала активной после добавления ингредиентов")
    
        return self.click_make_order()

    @allure.step("Проверить статус авторизации")
    def check_auth_status(self):
        try:
            return self.is_visible(self.locators.PERSONAL_ACCOUNT_BUTTON, timeout=2)
        except:
            return False
    
    @allure.step("Дождаться подтверждения заказа")
    def wait_for_order_confirmation(self, timeout=30):
        return self.is_visible(OrderModalLocators.ORDER_NUMBER, timeout)
    
    @allure.step("Получить номер созданного заказа")
    def get_created_order_number(self):
        try:
            order_number_element = self.find_element(OrderModalLocators.ORDER_NUMBER, timeout=5)
            return order_number_element.text
        except:
            return "0000"
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        if self.is_visible(OrderModalLocators.ORDER_MODAL_CLOSE, timeout=5):
            self.click(OrderModalLocators.ORDER_MODAL_CLOSE)
        return self
    
    @allure.step("Проверить наличие кнопки конструктора")
    def is_constructor_button_present(self):
        return self.is_present(self.locators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Проверить наличие кнопки ленты заказов")
    def is_order_feed_button_present(self):
        return self.is_present(self.locators.ORDER_FEED_BUTTON)
    
    @allure.step("Проверить наличие кнопки личного кабинета")
    def is_personal_account_button_present(self):
        return self.is_present(self.locators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Проверить наличие секции ингредиентов")
    def is_ingredients_section_present(self):
        return self.is_present(self.locators.INGREDIENTS_SECTION)
    
    @allure.step("Проверить наличие ингредиентов")
    def has_ingredients(self):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        return len(ingredients) > 0
    
    @allure.step("Проверить активность конструктора")
    def is_constructor_active(self):
        return self.is_present(self.locators.CONSTRUCTOR_ACTIVE)
    
    @allure.step("Проверить активность ленты заказов")
    def is_order_feed_active(self):
        return self.is_present(self.locators.ORDER_FEED_ACTIVE)
    
    @allure.step("Проверить наличие логотипа")
    def is_logo_present(self):
        return self.is_present(self.locators.LOGO)
    
    @allure.step("Кликнуть на логотип")
    def click_logo(self):
        self.click(self.locators.LOGO)
        return self.wait_for_page_loaded()
    
    @allure.step("Проверить загрузку главной страницы")
    def is_main_page_loaded(self):
        return self.is_present(self.locators.PAGE_TITLE)
    
    @allure.step("Проверить активность раздела булок")
    def is_buns_section_active(self):
        return self.is_present(self.locators.BUNS_SECTION_ACTIVE)
    
    @allure.step("Проверить активность раздела соусов")
    def is_sauces_section_active(self):
        return self.is_present(self.locators.SAUCES_SECTION_ACTIVE)
    
    @allure.step("Проверить активность раздела начинок")
    def is_fillings_section_active(self):
        return self.is_present(self.locators.FILLINGS_SECTION_ACTIVE)
    
    @allure.step("Проверить наличие булок")
    def has_buns_ingredients(self):
        buns = self.find_elements(self.locators.BUNS_INGREDIENTS)
        return len(buns) > 0
    
    @allure.step("Проверить наличие соусов")
    def has_sauces_ingredients(self):
        sauces = self.find_elements(self.locators.SAUCES_INGREDIENTS)
        return len(sauces) > 0
    
    @allure.step("Проверить наличие начинок")
    def has_fillings_ingredients(self):
        fillings = self.find_elements(self.locators.FILLINGS_INGREDIENTS)
        return len(fillings) > 0
    
    @allure.step("Дождаться видимости элемента")
    def wait_for_element_visible(self, locator, timeout=10):
        return self.wait.wait_for_element_visible(locator, timeout)
    
    @allure.step("Проверить, что кнопка заказа активна")
    def is_order_button_active(self):
        return self.is_visible(self.locators.ORDER_BUTTON_ACTIVE, timeout=5)