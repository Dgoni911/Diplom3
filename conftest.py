import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from helpers.wait_helpers import WaitHelpers


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", 
                    help="Browser to run tests: chrome or firefox")
    parser.addoption("--headless", action="store_true", 
                    help="Run tests in headless mode")
    parser.addoption("--base-url", action="store", 
                    default="https://stellarburgers.nomoreparties.site", 
                    help="Base URL for tests")
    parser.addoption("--timeout", action="store", default="30",
                    help="Default timeout for operations")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture(scope="session")
def global_timeout(request):
    return int(request.config.getoption("--timeout"))


@pytest.fixture
def browser(request, global_timeout):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference('useAutomationExtension', False)
        
        options.set_preference("browser.cache.disk.enable", False)
        options.set_preference("browser.cache.memory.enable", False)
        options.set_preference("browser.cache.offline.enable", False)
        options.set_preference("network.http.use-cache", False)
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    if browser_name == "firefox":
        driver.implicitly_wait(15)  
    else:
        driver.implicitly_wait(10)
    
    driver.set_page_load_timeout(global_timeout)
    driver.set_script_timeout(30)
    
    yield driver
    
    try:
        driver.quit()
    except Exception as e:
        print(f"Ошибка при закрытии браузера: {e}")


@pytest.fixture
def wait_helper(browser):
    return WaitHelpers(browser)


@pytest.fixture
def browser_helper(browser):
    from helpers.browser_helpers import BrowserHelpers
    return BrowserHelpers(browser)


@pytest.fixture
def element_helper(browser):
    from helpers.element_helpers import ElementHelpers
    return ElementHelpers(browser)


@pytest.fixture
def main_page(browser, base_url, wait_helper, browser_helper):
    from pages.main_page import MainPage
    page = MainPage(browser, base_url, wait_helper, browser_helper)
    page.open()
    return page


