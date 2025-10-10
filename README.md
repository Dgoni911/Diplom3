# Diplom3
Автотесты для UI

Косач Евгения 29-я когорта

pip install -r requirements.txt

# Запуск в Chrome (по умолчанию)
pytest

# Запуск в Firefox
pytest --browser=firefox

# Запуск с Allure отчетами
pytest --alluredir=allure-results
allure serve allure-results

├── .gitignore
├── requirements.txt
├── pytest.ini
├── conftest.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── main_page.py
│   ├── login_page.py
│   ├── registration_page.py
│   ├── profile_page.py
│   ├── constructor_page.py
│   └── order_feed_page.py
├── tests/
│   ├── __init__.py
│   ├── test_constructor.py
│   ├── test_order_feed.py
│   └── test_ingredients.py
├── locators/
│    ├── __init__.py
│    ├── main_page_locators.py
│    ├── constructor_locators.py
│    └── order_feed_locators.py
└── ├── helpers/
    ├── __init__.py
    ├── wait_helpers.py          
    ├── browser_helpers.py       
    └── element_helpers.py