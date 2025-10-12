from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
    BUNS_SECTION = (By.XPATH, "//div[./span[text()='Булки']]")
    SAUCES_SECTION = (By.XPATH, "//div[./span[text()='Соусы']]")
    FILLINGS_SECTION = (By.XPATH, "//div[./span[text()='Начинки']]")
    
    INGREDIENT_ITEM = (By.CSS_SELECTOR, "[class*='BurgerIngredient_ingredient']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "[class*='counter_counter__']")
    
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")