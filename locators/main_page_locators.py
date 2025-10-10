from selenium.webdriver.common.by import By


class MainPageLocators:
    
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
    
    
    INGREDIENT_ITEM = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter')]")
    
    
    CONSTRUCTOR_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close')]")
    INGREDIENT_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h3")