from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
    INGREDIENTS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    BUNS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']")
    SAUCES_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']")
    FILLINGS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']")
    
    BUNS_INGREDIENTS = (By.XPATH, "//h2[text()='Булки']/following-sibling::ul//a")
    SAUCES_INGREDIENTS = (By.XPATH, "//h2[text()='Соусы']/following-sibling::ul//a")
    FILLINGS_INGREDIENTS = (By.XPATH, "//h2[text()='Начинки']/following-sibling::ul//a")
    
    CONSTRUCTOR_ACTIVE = (By.XPATH, "//a[.//p[text()='Конструктор'] and contains(@class, 'active')]")
    ORDER_FEED_ACTIVE = (By.XPATH, "//a[.//p[text()='Лента Заказов'] and contains(@class, 'active')]")
    
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGIN_FORM = (By.XPATH, "//form[contains(@class, 'Auth_form')]")
    
    ORDER_FEED_SECTION = (By.XPATH, "//section[contains(@class, 'OrderFeed') or contains(@class, 'order-feed') or contains(@class, 'feed')]")