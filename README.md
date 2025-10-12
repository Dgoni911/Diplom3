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

stellarburgers-ui-tests/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── main_page.py
│   ├── constructor_page.py
│   ├── order_feed_page.py
│   ├── login_page.py
│   └── order_modal.py
├── locators/
│   ├── __init__.py
│   ├── base_locators.py
│   ├── main_page_locators.py
│   ├── constructor_locators.py
│   ├── order_feed_locators.py
│   ├── order_modal_locators.py
│   └── login_locators.py
├── helpers/
│   ├── __init__.py
│   ├── url_helper.py
│   ├── data_helper.py
│   ├── retry_helper.py
│   └── wait_helper.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_constructor.py
│   └── test_order_feed.py
├── utils/
│   ├── __init__.py
│   └── logger.py
├── __init__.py
├── requirements.txt
├── pytest.ini
├── run_tests.py
├── generate_report.py
├── test_imports.py
└── .gitignore
