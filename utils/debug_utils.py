import allure
from selenium.webdriver.common.by import By

def analyze_page_structure(driver, page_name=""):
    """Анализ структуры страницы для отладки"""
    print(f"\n=== ANALYZING PAGE STRUCTURE: {page_name} ===")
    print(f"URL: {driver.current_url}")
    print(f"Title: {driver.title}")
    
    elements_to_check = [
        ("Sections", "//section"),
        ("Main content", "//main"),
        ("Headers", "//h1 | //h2 | //h3"),
        ("Containers", "//div[contains(@class, 'container')]"),
        ("Any elements with 'feed'", "//*[contains(@class, 'feed')]"),
        ("Any elements with 'order'", "//*[contains(@class, 'order')]"),
        ("Lists", "//ul | //ol"),
        ("Total orders text", "//*[contains(text(), 'Выполнено за все время')]"),
        ("Today orders text", "//*[contains(text(), 'Выполнено за сегодня')]"),
    ]
    
    results = []
    for element_name, xpath in elements_to_check:
        try:
            elements = driver.find_elements(By.XPATH, xpath)
            if elements:
                results.append(f"✓ {element_name}: {len(elements)} elements found")
                for i, elem in enumerate(elements[:3]):
                    try:
                        class_attr = elem.get_attribute('class') or 'no-class'
                        text = elem.text[:50] + '...' if len(elem.text) > 50 else elem.text
                        results.append(f"  {i+1}. class='{class_attr}', text='{text}'")
                    except:
                        results.append(f"  {i+1}. [error getting details]")
            else:
                results.append(f"✗ {element_name}: No elements found")
        except Exception as e:
            results.append(f"✗ {element_name}: Error - {str(e)}")
    
    log_message = "\n".join(results)
    print(log_message)
    
    allure.attach(
        log_message,
        name=f"page_analysis_{page_name}",
        attachment_type=allure.attachment_type.TEXT
    )
    
    allure.attach(
        driver.get_screenshot_as_png(),
        name=f"analysis_screenshot_{page_name}",
        attachment_type=allure.attachment_type.PNG
    )
    
    return results