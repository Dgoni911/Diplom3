from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class WaitHelper:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
    
    def wait_for_ajax(self):
        try:
            self.wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
        except:
            pass  
    
    def wait_for_animation(self):
        try:
            self.wait.until(lambda driver: driver.execute_script(
                "return jQuery(':animated').length == 0"
            ))
        except:
            time.sleep(1)  
    
    def wait_for_page_ready(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        self.wait_for_ajax()
        self.wait_for_animation()