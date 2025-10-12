from selenium.webdriver.common.by import By

class ConstructorLocators:
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
    BUNS_SECTION = (By.XPATH, "//div[./span[text()='Булки']]")
    SAUCES_SECTION = (By.XPATH, "//div[./span[text()='Соусы']]")
    FILLINGS_SECTION = (By.XPATH, "//div[./span[text()='Начинки']]")