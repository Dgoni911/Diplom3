import allure
from helpers.wait_helpers import WaitHelpers
from helpers.browser_helpers import BrowserHelpers
from helpers.element_helpers import ElementHelpers


class BasePage:
    def __init__(self, driver, base_url, wait_helper=None, browser_helper=None, element_helper=None):
        self.driver = driver
        self.base_url = base_url
        self.wait = wait_helper or WaitHelpers(driver)
        self.browser = browser_helper or BrowserHelpers(driver)
        self.element = element_helper or ElementHelpers(driver)
    
    def open(self, url=""):
        with allure.step(f"Открыть страницу: {self.base_url}{url}"):
            full_url = self.base_url + url
            self.driver.get(full_url)
            self.wait.wait_for_page_load()
    
    def find_element(self, locator, timeout=15):
        return self.wait.wait_for_element(locator, timeout)
    
    def find_elements(self, locator, timeout=15):
        self.wait.wait_for_element(locator, timeout)  
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        return self.browser.safe_click(locator)
    
    def is_element_present(self, locator, timeout=5):
        return self.browser.is_element_present(locator, timeout)
    
    def get_text(self, locator):
        return self.element.get_element_text(locator)
    
    def drag_and_drop(self, source_locator, target_locator):
        self.browser.safe_drag_and_drop(source_locator, target_locator)