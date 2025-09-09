import os
import allure
import pytest
from pages.professional_login_page import ProfessionalLoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
@allure.title("Professional login test (valid credentials)")
def test_professional_login(driver):
    page = ProfessionalLoginPage(driver)
    page.open()
    
    page.set_username("testuser")
    page.set_password("password123")
    page.submit()
    
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "message"), "Login successful!"))
    
    assert "Professional Login Page" in driver.title
    
@allure.title("Professional login test (invalid credentials)")
def test_invalid_login(driver):
    page = ProfessionalLoginPage(driver)
    page.open()
    
    page.set_username("bad_user")
    page.set_password("wrong_password")
    page.submit()
    
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "message"), "Invalid credentials. Please try again."))
    
    message = page.get_message()
    assert "Invalid credentials. Please try again." in message