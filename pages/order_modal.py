import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.order_modal_locators import OrderModalLocators

class OrderModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        checks = [
            OrderModalLocators.INGREDIENT_DETAILS,
            OrderModalLocators.MODAL,
            OrderModalLocators.MODAL_CONTENT,
        ]
        
        for check in checks:
            if self._is_element_visible(check, timeout=1):
                return True
        return False
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        methods = [
            self._close_by_button,
            self._close_by_overlay, 
            self._close_by_escape,
            self._close_by_css
        ]
        
        for method in methods:
            if method():
                self.wait.until(EC.invisibility_of_element_located(OrderModalLocators.MODAL))
                return True
        return False
    
    @allure.step("Принудительно закрыть модальное окно")
    def force_close_modal(self):
        methods = [
            self.close_modal,
            self._close_by_js_force,
        ]
        
        for method in methods:
            try:
                if method():
                    if not self.is_modal_visible():
                        return True
            except Exception:
                continue
        return False
    
    def _close_by_button(self):
        if self.is_visible(OrderModalLocators.MODAL_CLOSE, timeout=3):
            self.click(OrderModalLocators.MODAL_CLOSE)
            return True
        return False
    
    def _close_by_overlay(self):
        if self.is_visible(OrderModalLocators.MODAL_OVERLAY, timeout=3):
            overlays = self.find_elements(OrderModalLocators.MODAL_OVERLAY)
            for overlay in overlays:
                if overlay.is_displayed():
                    self.execute_script("arguments[0].click();", overlay)
                    return True
        return False
    
    def _close_by_escape(self):
        try:
            active_element = self.driver.switch_to.active_element
            active_element.send_keys(Keys.ESCAPE)
            return True
        except Exception:
            return False
    
    def _close_by_css(self):
        try:
            self.execute_script("""
                var modals = document.querySelectorAll('div[class*=\"Modal_modal__\"]');
                for (var i = 0; i < modals.length; i++) {
                    modals[i].style.display = 'none';
                }
                var overlays = document.querySelectorAll('div[class*=\"Modal_modal_overlay__\"]');
                for (var i = 0; i < overlays.length; i++) {
                    overlays[i].style.display = 'none';
                }
            """)
            return True
        except Exception:
            return False
    
    def _close_by_js_force(self):
        try:
            scripts = [
                "var elements = document.querySelectorAll('div.Modal_modal__, div.Modal_modal_overlay__'); elements.forEach(function(el) { el.remove(); });",
                "var elements = document.querySelectorAll('div[class*=\"Modal\"]'); elements.forEach(function(el) { el.style.display = 'none'; el.style.visibility = 'hidden'; });",
                "document.body.style.overflow = 'auto';",
                "var buttons = document.querySelectorAll('button[class*=\"close\"]'); buttons.forEach(function(btn) { btn.click(); });",
            ]
            
            for script in scripts:
                try:
                    self.execute_script(script)
                except:
                    continue
            return True
        except:
            return False
    
    def _is_element_visible(self, locator, timeout=10):
        try:
            self.wait.wait_for_element_visible(locator, timeout)
            return True
        except TimeoutException:
            return False