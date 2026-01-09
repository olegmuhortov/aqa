# Автотесты для сайта SauceDemo

## Локальный запуск

### Клонирование репозитория
git clone <repository-url>
cd saucedemo-test-project

### Установка зависимостей
pip install -r requirements.txt

### Запуск тестов
pytest tests/

### Запуск тестов с генерацией Allure отчетов
pytest tests/ --alluredir=./allure-results

allure serve ./allure-results
