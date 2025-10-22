import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.order_modal_locators import OrderModalLocators

class OrderModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.is_visible(OrderModalLocators.MODAL, timeout=3) or self.is_visible(OrderModalLocators.INGREDIENT_DETAILS, timeout=3)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        methods = [
            self._close_by_close_button,
            self._close_by_escape,
            self._close_by_overlay_click,
            self._close_by_overlay_js,
            self._close_by_css_hide
        ]
        
        for method in methods:
            try:
                if method():
                    if self._wait_for_modal_hidden():
                        return True
            except Exception:
                continue
        
        return False
    
    @allure.step("Принудительно закрыть модальное окно")
    def force_close_modal(self):
        try:
            scripts = [
                """
                var modals = document.querySelectorAll('div[class*="modal"], div[class*="Modal"]');
                modals.forEach(function(modal) {
                    modal.remove();
                });
                """,
                """
                var elements = document.querySelectorAll('div[class*="modal"], div[class*="Modal"]');
                elements.forEach(function(el) {
                    el.style.display = 'none';
                    el.style.visibility = 'hidden';
                    el.style.opacity = '0';
                });
                """,
                """
                var overlays = document.querySelectorAll('div[class*="overlay"], div[class*="Overlay"]');
                overlays.forEach(function(overlay) {
                    overlay.style.display = 'none';
                    overlay.style.visibility = 'hidden';
                    overlay.remove();
                });
                """,
                """
                document.body.style.overflow = 'auto';
                document.documentElement.style.overflow = 'auto';
                document.body.style.position = 'static';
                """
            ]
            
            for script in scripts:
                try:
                    self.execute_script(script)
                except:
                    continue
            
            self.execute_script("""
                // Очищаем все возможные модальные элементы
                var selectors = [
                    '[class*="modal"]',
                    '[class*="Modal"]', 
                    '[role="dialog"]',
                    '.modal',
                    '.Modal',
                    '.modal-overlay',
                    '.Modal_overlay'
                ];
                
                selectors.forEach(function(selector) {
                    var elements = document.querySelectorAll(selector);
                    elements.forEach(function(el) {
                        el.style.display = 'none';
                        el.style.visibility = 'hidden';
                        el.style.opacity = '0';
                        el.remove();
                    });
                });
                
                // Восстанавливаем body
                document.body.style.overflow = 'auto';
                document.body.classList.remove('modal-open', 'Modal_open');
            """)
            
            return self._wait_for_modal_hidden()
            
        except Exception:
            return False
    
    def _wait_for_modal_hidden(self, timeout=5):
        try:
            self.wait.wait_for_element_not_visible(OrderModalLocators.MODAL, timeout)
            return True
        except TimeoutException:
            try:
                self.wait.wait_for_element_not_visible(OrderModalLocators.INGREDIENT_DETAILS, timeout)
                return True
            except TimeoutException:
                return False
    
    def _close_by_close_button(self):
        try:
            if self.is_visible(OrderModalLocators.MODAL_CLOSE, timeout=2):
                close_button = self.find_element(OrderModalLocators.MODAL_CLOSE)
                try:
                    close_button.click()
                except:
                    self.execute_script("arguments[0].click();", close_button)
                return True
        except:
            pass
        return False
    
    def _close_by_escape(self):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            return True
        except:
            return False
    
    def _close_by_overlay_click(self):
        try:
            if self.is_visible(OrderModalLocators.MODAL_OVERLAY, timeout=2):
                overlays = self.find_elements(OrderModalLocators.MODAL_OVERLAY)
                for overlay in overlays:
                    if overlay.is_displayed():
                        self.execute_script("arguments[0].click();", overlay)
                        return True
        except:
            pass
        return False
    
    def _close_by_overlay_js(self):
        try:
            self.execute_script("""
                var overlays = document.querySelectorAll('div[class*="overlay"], div[class*="Overlay"]');
                for (var i = 0; i < overlays.length; i++) {
                    if (overlays[i].offsetParent !== null) {
                        overlays[i].click();
                        break;
                    }
                }
            """)
            return True
        except:
            return False
    
    def _close_by_css_hide(self):
        try:
            self.execute_script("""
                // Скрываем все модальные элементы
                var modals = document.querySelectorAll('div[class*="modal"], div[class*="Modal"]');
                modals.forEach(function(modal) {
                    modal.style.display = 'none';
                });
                
                // Скрываем overlay
                var overlays = document.querySelectorAll('div[class*="overlay"], div[class*="Overlay"]');
                overlays.forEach(function(overlay) {
                    overlay.style.display = 'none';
                });
            """)
            return True
        except:
            return False