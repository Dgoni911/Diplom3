import allure
import time
from selenium.webdriver.common.by import By
from helpers.wait_helper import WaitHelper
from helpers.url_helper import UrlHelper
from locators.main_page_locators import MainPageLocators
from locators.order_modal_locators import OrderModalLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)
        self.url_helper = UrlHelper()
        self.locators = MainPageLocators()  
    
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.url_helper.get_base_url())
        self.wait.wait_for_page_load()
        return self
    
    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_loaded(self):
        self.wait.wait_for_page_load()
        
        possible_elements = [
            MainPageLocators.CONSTRUCTOR_BUTTON,
            MainPageLocators.INGREDIENTS_SECTION,
            MainPageLocators.ORDER_BUTTON,
            (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"),
            (By.XPATH, "//p[contains(text(), 'Конструктор')]"),
        ]
        
        for element in possible_elements:
            try:
                self.wait.wait_for_element_present(element, timeout=5)
                return True
            except:
                continue
        
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="page_loaded_failed",
            attachment_type=allure.attachment_type.PNG
        )
        raise Exception("Не удалось дождаться загрузки главной страницы")
    
    @allure.step("Кликнуть на конструктор")
    def click_constructor(self):
        try:
            self.wait.wait_for_element_clickable(MainPageLocators.CONSTRUCTOR_BUTTON).click()
        except:
            constructor_alt = (By.XPATH, "//p[contains(text(), 'Конструктор')]/parent::a")
            self.wait.wait_for_element_clickable(constructor_alt).click()
    
    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        try:
            self.wait.wait_for_element_clickable(MainPageLocators.ORDER_FEED_BUTTON).click()
        except:
            order_feed_alt = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]/parent::a")
            self.wait.wait_for_element_clickable(order_feed_alt).click()
        self.wait.wait_for_page_load()
    
    @allure.step("Кликнуть на личный кабинет")
    def click_personal_account(self):
        try:
            self.wait.wait_for_element_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        except:
            personal_account_alt = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]/parent::a")
            self.wait.wait_for_element_clickable(personal_account_alt).click()
        self.wait.wait_for_page_load()
    
    @allure.step("Кликнуть на ингредиент {index}")
    def click_ingredient(self, index=0):
        ingredients = self.wait.wait_for_element_present(MainPageLocators.INGREDIENT_ITEM)
        all_ingredients = self.driver.find_elements(*MainPageLocators.INGREDIENT_ITEM)
        
        if all_ingredients and index < len(all_ingredients):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", all_ingredients[index])
            all_ingredients[index].click()
            self.wait.wait_for_element_visible(OrderModalLocators.INGREDIENT_DETAILS, timeout=5)
    
    @allure.step("Проверить видимость модального окна ингредиента")
    def is_ingredient_modal_visible(self):
        try:
            self.wait.wait_for_element_visible(OrderModalLocators.INGREDIENT_DETAILS, timeout=3)
            return True
        except:
            return False
    
    @allure.step("Кликнуть 'Сделать заказ'")
    def click_make_order(self):
        self.wait.wait_for_element_clickable(MainPageLocators.ORDER_BUTTON).click()
    
    @allure.step("Кликнуть на раздел булок")
    def click_buns_section(self):
        self.wait.wait_for_element_clickable(MainPageLocators.BUNS_SECTION).click()
    
    @allure.step("Кликнуть на раздел соусов")
    def click_sauces_section(self):
        self.wait.wait_for_element_clickable(MainPageLocators.SAUCES_SECTION).click()
    
    @allure.step("Кликнуть на раздел начинок")
    def click_fillings_section(self):
        self.wait.wait_for_element_clickable(MainPageLocators.FILLINGS_SECTION).click()
    
    
    @allure.step("Проверить наличие элемента {locator}")
    def is_element_present(self, locator, timeout=5):
        try:
            self.wait.wait_for_element_present(locator, timeout)
            return True
        except:
            return False
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        return self.wait.wait_for_element_present(locator, timeout)
    
    @allure.step("Найти элементы {locator}")
    def find_elements(self, locator, timeout=10):
        return self.driver.find_elements(*locator)
    
    @allure.step("Кликнуть на элемент {locator}")
    def click_element(self, locator):
        element = self.wait.wait_for_element_clickable(locator)
        element.click()
    
    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_element_visible(self, locator, timeout=10):
        return self.wait.wait_for_element_visible(locator, timeout)
    
    @allure.step("Добавить ингредиент в конструктор по индексу {index}")
    def add_ingredient_to_constructor(self, index):
        ingredients = self.driver.find_elements(*MainPageLocators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            ingredients[index].click()
    
    @allure.step("Создать тестовый заказ")
    def create_test_order(self):
        self.add_ingredient_to_constructor(0)  
        self.add_ingredient_to_constructor(5)  
        self.add_ingredient_to_constructor(10) 
        
        self.click_make_order()
    
    @allure.step("Дождаться подтверждения заказа")
    def wait_for_order_confirmation(self, timeout=30):
        try:
            self.wait.wait_for_element_visible((By.XPATH, "//p[contains(@class, 'digits-large')]"), timeout)
            return True
        except:
            return False
    
    @allure.step("Получить номер созданного заказа")
    def get_created_order_number(self):
        try:
            order_number_element = self.wait.wait_for_element_visible((By.XPATH, "//p[contains(@class, 'digits-large')]"), timeout=5)
            return order_number_element.text
        except:
            return "0000"  
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        try:
            close_button = self.wait.wait_for_element_clickable((By.XPATH, "//button[contains(@class, 'Modal_close')]"), timeout=5)
            close_button.click()
            return True
        except:
            return False