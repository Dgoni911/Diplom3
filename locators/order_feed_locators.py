from selenium.webdriver.common.by import By


class OrderFeedLocators:
    
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]//li[contains(@class, 'OrderFeed_inProgress')]")
    
    
    ORDER_CARDS = (By.XPATH, "//div[contains(@class, 'OrderHistory_list')]//li")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")