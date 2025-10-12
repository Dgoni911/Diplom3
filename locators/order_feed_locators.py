from selenium.webdriver.common.by import By

class OrderFeedLocators:
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[./li[text()='В работе:']]//li[contains(@class, 'OrderFeed_number')]")
    
    ORDER_ITEMS = (By.XPATH, "//div[contains(@class, 'OrderHistory_list')]//li")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'digits-default')]")