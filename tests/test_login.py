import os
import allure
import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
@allure.title("Valid login should succeed")
def test_valid_login(driver):
    base_url = "https://the-internet.herokuapp.com"
    page = LoginPage(driver, base_url)
    page.open()
    
    username = os.getenv("VALID_USERNAME", "tomsmith")
    password = os.getenv("VALID_PASSWORD", "SuperSecretPassword!")
    
    page.set_username(username)
    page.set_password(password)
    page.submit()
    
    # Wait for the secure area page to load by checking for its header
    secure_area_header = (By.CSS_SELECTOR, "h2")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(secure_area_header)
    )
    
    success_message = page.get_success_message()
    assert "You logged into a secure area!" in success_message
    
    # The title of the secure area page is still "The Internet", so we check for that.
    assert "The Internet" in driver.title

@allure.title("Invalid login shows error")
def test_invalid_login(driver):
    base_url = "https://the-internet.herokuapp.com"
    page = LoginPage(driver, base_url)
    page.open()
    
    page.set_username("bad_user")
    page.set_password("bad_pass")
    page.submit()
    
    error_message = page.get_error_message()
    assert "Your username is invalid!" in error_message or "Your password is invalid!" in error_message