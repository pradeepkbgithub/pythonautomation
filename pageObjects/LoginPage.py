import time

from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    login_button_xpath = "//button[@type='submit']"
    userlink_xpath = "//a[@class='userlink']"
    login_link = "//a[@class='ico-login']"
    logout_link = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username.strip())

    def setPassword(self, password):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password.strip())

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def clickUserLink(self):
        self.driver.find_element(By.XPATH, self.userlink_xpath).click()

    def clickLoginLink(self):
        self.driver.find_element(By.XPATH, self.login_link).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_link).click()
