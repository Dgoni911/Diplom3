from selenium.webdriver.common.by import By


class ConstructorLocators:
    
    BUN_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    SAUCE_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[6]")
    FILLING_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[11]")
    
    
    BUN_DROP_ZONE = (By.XPATH, "(//div[contains(@class, 'BurgerConstructor_basket')]//div[contains(@class, 'BurgerConstructor_element')])[1]")
    INGREDIENTS_DROP_ZONE = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]//ul")
    
    
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter__')]")