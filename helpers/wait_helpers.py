import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.remote.webdriver import WebDriver


class WaitHelpers:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    @allure.step("Ожидание полной загрузки страницы")
    def wait_for_page_load(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            
            if "firefox" in self.driver.name.lower():
                self._wait_for_firefox_specific_loading(timeout)
                
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="page_load_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Страница не загрузилась за {timeout} секунд")
    
    def _wait_for_firefox_specific_loading(self, timeout):
        selectors_to_wait = [
            "[class*='loading']",
            "[class*='spinner']",
            "[class*='progress']"
        ]
        
        for selector in selectors_to_wait:
            try:
                WebDriverWait(self.driver, 5).until(
                    lambda driver: len(driver.find_elements("css selector", selector)) == 0
                )
            except TimeoutException:
                pass
        
        time.sleep(2)
    
    @allure.step("Ожидание появления элемента")
    def wait_for_element(self, locator, timeout=15, poll_frequency=0.5):
        def _find_element(driver):
            try:
                element = driver.find_element(*locator)
                return element if element.is_displayed() else None
            except StaleElementReferenceException:
                return None
            except Exception:
                return None
        
        return WebDriverWait(self.driver, timeout, poll_frequency).until(
            _find_element,
            message=f"Элемент {locator} не появился за {timeout} секунд"
        )
    
    @allure.step("Ожидание кликабельности элемента")
    def wait_for_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не стал кликабельным за {timeout} секунд"
        )
    
    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator),
            message=f"Элемент {locator} не исчез за {timeout} секунд"
        )
    
    @allure.step("Ожидание появления текста в элементе")
    def wait_for_text_in_element(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Текст '{text}' не появился в элементе {locator} за {timeout} секунд"
        )
    
    @allure.step("Ожидание обновления данных (polling)")
    def wait_for_condition(self, condition_func, timeout=30, poll_interval=1, description=""):
        end_time = time.time() + timeout
        last_exception = None
        
        while time.time() < end_time:
            try:
                if condition_func():
                    return True
            except Exception as e:
                last_exception = e
            
            time.sleep(poll_interval)
        
        if last_exception:
            raise TimeoutException(
                f"Условие не выполнено за {timeout} секунд. Последняя ошибка: {last_exception}"
            )
        raise TimeoutException(f"Условие не выполнено за {timeout} секунд: {description}")