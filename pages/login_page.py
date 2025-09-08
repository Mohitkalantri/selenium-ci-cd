import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    PATH = "/login"
    
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    
    # Updated locator for the login button.
    # It looks for a button that contains the text 'Login' inside an <i> tag.
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']") 
    
    SUCCESS_MESSAGE = (By.ID, "flash")
    ERROR_MESSAGE = (By.ID, "flash")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + self.PATH)

    def set_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USERNAME)).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def set_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD)).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_success_message(self):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text
        except:
            return ""

    def get_error_message(self):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
        except:
            return ""