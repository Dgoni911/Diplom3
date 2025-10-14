import allure
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_modal_locators import OrderModalLocators

class OrderModal:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        checks = [
            OrderModalLocators.INGREDIENT_DETAILS,
            OrderModalLocators.MODAL,
            OrderModalLocators.MODAL_CONTENT,
        ]

        for check in checks:
            try:
                if self._is_element_present(check, timeout=1):
                    element = self._find_element(check, timeout=1)
                    if element.is_displayed():
                        return True
            except:
                continue
        return False

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        with allure.step("Попытка закрыть модальное окно стандартными методами"):
            if self._close_by_button():
                return True
            if self._close_by_overlay():
                return True
            if self._close_by_escape():
                return True
            if self._close_by_css():
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
                result = method()
                if result:
                    time.sleep(2)
                    if not self.is_modal_visible():
                        return True
            except Exception:
                continue
        return False

    def _close_by_button(self):
        try:
            if self._is_element_present(OrderModalLocators.MODAL_CLOSE, timeout=3):
                close_button = self._find_element(OrderModalLocators.MODAL_CLOSE)
                self.driver.execute_script("arguments[0].click();", close_button)
                time.sleep(1)
                return True
        except Exception:
            return False
        return False

    def _close_by_overlay(self):
        try:
            if self._is_element_present(OrderModalLocators.MODAL_OVERLAY, timeout=3):
                overlays = self._find_elements(OrderModalLocators.MODAL_OVERLAY)
                for overlay in overlays:
                    if overlay.is_displayed():
                        self.driver.execute_script("arguments[0].click();", overlay)
                        time.sleep(1)
                        return True
        except Exception:
            return False
        return False

    def _close_by_escape(self):
        try:
            active_element = self.driver.switch_to.active_element
            active_element.send_keys(Keys.ESCAPE)
            time.sleep(1)
            return True
        except Exception:
            return False

    def _close_by_css(self):
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
            time.sleep(1)
            return True
        except Exception:
            return False

    def _close_by_js_force(self):
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

    @allure.step("Найти элемент {locator} с таймаутом {timeout}")
    def _find_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти элементы {locator} с таймаутом {timeout}")
    def _find_elements(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Проверить наличие элемента {locator} с таймаутом {timeout}")
    def _is_element_present(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False