# Автотесты для сайта SauceDemo

## Локальный запуск

### Установка зависимостей
pip install -r requirements.txt

### Запуск тестов
pytest tests/

### Запуск тестов с генерацией Allure отчетов
pytest tests/ --alluredir=./allure-results

allure serve ./allure-results
