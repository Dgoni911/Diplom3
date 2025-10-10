import time
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from helpers.wait_helpers import WaitHelpers


class BrowserHelpers:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelpers(driver)
    
    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element_or_locator):
        if hasattr(element_or_locator, 'location'):
            element = element_or_locator
        else:
            element = self.wait.wait_for_element(element_or_locator)
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element
    
    @allure.step("Клик с проверкой успешности")
    def safe_click(self, locator, timeout=15):
        element = self.wait.wait_for_clickable(locator, timeout)
        
        try:
            element.click()
            return True
        except Exception as e:
            try:
                self.driver.execute_script("arguments[0].click();", element)
                return True
            except Exception as js_e:
                allure.attach(
                    f"Ошибка клика: {e}, JS ошибка: {js_e}",
                    name="click_error",
                    attachment_type=allure.attachment_type.TEXT
                )
                raise
    
    @allure.step("Перетаскивание с проверкой")
    def safe_drag_and_drop(self, source_locator, target_locator):
        source = self.wait.wait_for_element(source_locator)
        target = self.wait.wait_for_element(target_locator)
        
        self.scroll_to_element(source)
        self.scroll_to_element(target)
        
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()
        
        time.sleep(1)
    
    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()
        self.wait.wait_for_page_load()
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        self.wait.wait_for_page_load()
        return self.driver.current_url
    
    @allure.step("Проверить наличие элемента")
    def is_element_present(self, locator, timeout=5):
        try:
            self.wait.wait_for_element(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    @allure.step("Сделать скриншот")
    def take_screenshot(self, name="screenshot"):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    
    @allure.step("Кликнуть на элемент напрямую")
    def safe_click_element(self, element):
        try:
            element.click()
        except Exception as e:
            try:
                self.driver.execute_script("arguments[0].click();", element)
            except Exception as js_e:
                raise Exception(f"Не удалось кликнуть на элемент: {e}, JS: {js_e}")