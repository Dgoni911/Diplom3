from selenium.webdriver.common.by import By

class OrderModalLocators:
    MODAL = (By.XPATH, "//div[@class='Modal_modal__P3_V5']")
    MODAL_OVERLAY = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")
    MODAL_CLOSE = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_NAME = (By.XPATH, "//h2[text()='Детали ингредиента']/following-sibling::p")
    
    MODAL_CONTAINER = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']")
    MODAL_CONTENT = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']")
    
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal') and .//p[contains(text(), 'идентификатор заказа')]]")
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'digits-large')]")
    ORDER_STATUS = (By.XPATH, "//p[contains(@class, 'order-status')]")
    ORDER_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_close')]")
    
    ANY_MODAL = (By.XPATH, "//div[contains(@class, 'modal') or contains(@class, 'Modal')]")
    ANY_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'close') or contains(@class, 'Modal_close')]")