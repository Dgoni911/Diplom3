from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER_FEED_SECTION = (By.XPATH, "//section[contains(@class, 'OrderFeed')]")
    ORDER_FEED_CONTAINER = (By.XPATH, "//div[contains(@class, 'OrderFeed_container')]")
    ORDER_FEED_LIST = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderList')]")
    
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[./li[text()='В работе:']]//li[contains(@class, 'OrderFeed_number')] | //ul[contains(@class, 'OrderFeed_orderList')]//li[contains(@class, 'pending')]")
    
    ORDER_ITEMS = (By.XPATH, "//div[contains(@class, 'OrderHistory_list')]//li")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'digits-default')]")
    
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/') and contains(@class, 'constructor')]")
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'logo')]")
    
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//p[contains(@class, 'digits')]")
    MODAL_ORDER_STATUS = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//p[contains(@class, 'status')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//button[contains(@class, 'close')]")
    
    ORDER_FEED_ALT1 = (By.XPATH, "//main[contains(@class, 'OrderFeed')]")
    ORDER_FEED_ALT2 = (By.XPATH, "//div[contains(@class, 'order-feed')]")
    ORDER_FEED_ALT3 = (By.XPATH, "//section[.//h1[contains(text(), 'Лента заказов')]]")
    
    ORDER_STATS_SECTION = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderStats')]")
    READY_ORDERS_SECTION = (By.XPATH, "//div[contains(@class, 'OrderFeed_readyOrders')]")
    IN_PROGRESS_SECTION = (By.XPATH, "//div[contains(@class, 'OrderFeed_inProgress')]")