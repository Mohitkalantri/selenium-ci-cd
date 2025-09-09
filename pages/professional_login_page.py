import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfessionalLoginPage:
    # Set the PATH to the local file path of your HTML page
    PATH = "file:///C:/Users/mohit/Documents/selenium-ci-cd/index.html"
    
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    
    MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.PATH)

    def set_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USERNAME)).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def set_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD)).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_message(self):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.MESSAGE)).text
        except:
            return ""