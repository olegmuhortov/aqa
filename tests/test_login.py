import allure
import pytest
from pages.login_page import LoginPage

@allure.epic("Авторизация на сайте Saucedemo")
@allure.feature("Функциональность логина")
class TestLogin:
    
    @allure.story("Позитивные сценарии")
    @allure.title("Успешная авторизация валидными данными")
    @allure.description("Проверка входа с корректными учетными данными standard_user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, driver):
      
        login_page = LoginPage(driver).open()
        
        with allure.step("Ввести логин и пароль"):
            login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Проверить редирект на страницу инвентаря"):
            assert "/inventory.html" in login_page.get_current_url()
        
        with allure.step("Проверить отображение страницы товаров"):
            assert login_page.is_inventory_page_displayed()
    
    @allure.story("Негативные сценарии")
    @allure.title("Авторизация с некорректным паролем")
    @allure.description("Проверка ошибки при вводе неправильного пароля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_wrong_password(self, driver):

        login_page = LoginPage(driver).open()
        
        with allure.step("Ввести логин и неверный пароль"):
            login_page.login("standard_user", "wrong_password")
        
        with allure.step("Проверить сообщение об ошибке"):
            error_message = login_page.get_error_message()
            assert "Username and password do not match" in error_message
        
        with allure.step("Проверить что остались на странице логина"):
            assert login_page.is_login_page_displayed()
    
    @allure.story("Негативные сценарии")
    @allure.title("Авторизация заблокированным пользователем")
    @allure.description("Проверка ошибки при попытке входа заблокированным пользователем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_locked_out_user(self, driver):
        """Тест авторизации заблокированного пользователя"""
        login_page = LoginPage(driver).open()
        
        with allure.step("Ввести данные заблокированного пользователя"):
            login_page.login("locked_out_user", "secret_sauce")
        
        with allure.step("Проверить сообщение об ошибке блокировки"):
            error_message = login_page.get_error_message()
            assert "Sorry, this user has been locked out" in error_message
        
        with allure.step("Проверить что остались на странице логина"):
            assert login_page.is_login_page_displayed()
    
    @allure.story("Негативные сценарии")
    @allure.title("Авторизация с пустыми полями")
    @allure.description("Проверка валидации пустых полей")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_fields(self, driver):
      
        login_page = LoginPage(driver).open()
        
        with allure.step("Нажать кнопку Login без заполнения полей"):
            login_page.click_login()
        
        with allure.step("Проверить сообщение об ошибке"):
            error_message = login_page.get_error_message()
            assert "Username is required" in error_message
        
        with allure.step("Проверить что остались на странице логина"):
            assert login_page.is_login_page_displayed()
    
    @allure.story("Позитивные сценарии")
    @allure.title("Авторизация пользователем с задержками")
    @allure.description("Проверка входа пользователем performance_glitch_user с задержками")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_performance_glitch_user(self, driver):
      
        login_page = LoginPage(driver).open()
        
        with allure.step("Ввести данные пользователя с возможными задержками"):
            login_page.login("performance_glitch_user", "secret_sauce")
        
        with allure.step("Дождаться редиректа на страницу инвентаря"):
            assert "/inventory.html" in login_page.get_current_url()
        
        with allure.step("Проверить отображение страницы товаров"):
            assert login_page.is_inventory_page_displayed()
