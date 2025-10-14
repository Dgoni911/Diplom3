from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class WaitHelper:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
    
    @allure.step("Ожидание полной загрузки страницы")
    def wait_for_page_load(self, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    
    @allure.step("Ожидание загрузки страницы с проверкой нескольких элементов")
    def wait_for_page_with_elements(self, elements, timeout=None):
        """Ожидание загрузки страницы с проверкой нескольких элементов"""
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        
        def page_loaded(driver):
            if driver.execute_script("return document.readyState") != "complete":
                return False
            
            for element in elements:
                try:
                    if driver.find_element(*element):
                        return True
                except:
                    continue
            return False
        
        return wait.until(page_loaded)
    
    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_element_visible(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Ожидание присутствия элемента {locator} в DOM")
    def wait_for_element_present(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Ожидание появления текста '{text}' в элементе {locator}")
    def wait_for_text_in_element(self, locator, text, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.text_to_be_present_in_element(locator, text))
    
    @allure.step("Ожидание появления текста '{text}' в URL")
    def wait_for_url_contains(self, text, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.url_contains(text))
    
    @allure.step("Ожидание исчезновения элемента {locator}")
    def wait_for_element_not_visible(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.invisibility_of_element_located(locator))