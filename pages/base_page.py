from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from locators.base_locators import BaseLocators
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
    
    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    def is_element_present(self, locator, timeout=5):
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_element_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    def close_modal(self):
        """Улучшенное закрытие модального окна"""
        from locators.order_modal_locators import OrderModalLocators
        
        print("🔧 Пытаемся закрыть модальное окно...")
        
        if self.is_element_present(OrderModalLocators.MODAL_CLOSE, timeout=3):
            try:
                close_button = self.find_element(OrderModalLocators.MODAL_CLOSE)
                print(f"✅ Нашли кнопку закрытия: {close_button.get_attribute('class')}")
                
                self.driver.execute_script("arguments[0].click();", close_button)
                print("✅ Кликнули через JavaScript")
                time.sleep(1)
                return True
            except Exception as e:
                print(f"❌ Ошибка при клике через JS: {e}")
        
        if self.is_element_present(OrderModalLocators.MODAL_OVERLAY, timeout=3):
            try:
                overlays = self.find_elements(OrderModalLocators.MODAL_OVERLAY)
                for overlay in overlays:
                    if overlay.is_displayed():
                        self.driver.execute_script("arguments[0].click();", overlay)
                        print("✅ Кликнули по overlay через JavaScript")
                        time.sleep(1)
                        return True
            except Exception as e:
                print(f"❌ Ошибка при клике по overlay: {e}")
        
        try:
            active_element = self.driver.switch_to.active_element
            active_element.send_keys(Keys.ESCAPE)
            print("✅ Отправили ESC в активный элемент")
            time.sleep(1)
            return True
        except Exception as e:
            print(f"❌ Ошибка при отправке ESC: {e}")
        
        try:
            self.driver.execute_script("""
                var modals = document.querySelectorAll('div[class*=\"Modal_modal__P3_V5\"]');
                for (var i = 0; i < modals.length; i++) {
                    modals[i].style.display = 'none';
                }
                var overlays = document.querySelectorAll('div[class*=\"Modal_modal_overlay__x2ZCr\"]');
                for (var i = 0; i < overlays.length; i++) {
                    overlays[i].style.display = 'none';
                }
            """)
            print("✅ Скрыли модальные окна через CSS")
            time.sleep(1)
            return True
        except Exception as e:
            print(f"❌ Ошибка при скрытии через CSS: {e}")
        
        return False
    
    def force_close_modal(self):
        from locators.order_modal_locators import OrderModalLocators
        
        print("🔄 Принудительное закрытие модального окна...")
        
        methods = [
            self.close_modal,  
            self.close_modal_by_js_force,  
        ]
        
        for method in methods:
            try:
                result = method()
                if result:
                    
                    time.sleep(2)
                    if not self.is_modal_visible():
                        print("✅ Модальное окно закрыто")
                        return True
            except Exception as e:
                print(f"❌ Ошибка в методе {method.__name__}: {e}")
                continue
        
        return False
    
    def close_modal_by_js_force(self):
        try:
            scripts = [
                "var elements = document.querySelectorAll('div.Modal_modal__P3_V5, div.Modal_modal_overlay__x2ZCr'); elements.forEach(function(el) { el.remove(); });",
                "var elements = document.querySelectorAll('div[class*=\"Modal\"]'); elements.forEach(function(el) { el.style.display = 'none'; el.style.visibility = 'hidden'; });",
                "document.body.style.overflow = 'auto'; document.documentElement.style.overflow = 'auto';",
                "var buttons = document.querySelectorAll('button[class*=\"close\"]'); buttons.forEach(function(btn) { btn.click(); });",
            ]
            
            for script in scripts:
                try:
                    self.driver.execute_script(script)
                    time.sleep(0.5)
                except:
                    continue
            
            return True
        except:
            return False
    
    def is_modal_visible(self):
        from locators.order_modal_locators import OrderModalLocators
        
        checks = [
            OrderModalLocators.INGREDIENT_DETAILS,
            OrderModalLocators.MODAL,
            OrderModalLocators.MODAL_CONTENT,
        ]
        
        for check in checks:
            if self.is_element_present(check, timeout=2):
                return True
        
        return False