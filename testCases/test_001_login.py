import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.get_application_url()  # "https://www.nopcommerce.com/en/login"
    username = ReadConfig.get_user_email()  # "test"
    password = ReadConfig.get_password()  # "test"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("************ test_home_page_title *************")
        self.logger.info("************ Verifying Home Page Title ********")
        self.driver = setup  # webdriver.chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print("===================== " + act_title)

        if act_title == "Your store. Login":  # "Store Demo - nopCommerce":
            assert True
            self.driver.close()
            self.logger.info("************* Home page title is passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_home_page_title.png")
            self.driver.close()
            self.logger.info('************* Home page title is failed')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info('********** Verifying title after login ******** ')
        try:
            self.driver = setup  # webdriver.chrome()
            self.driver.get(self.baseURL)
            self.loginObj = LoginPage(self.driver)
            self.loginObj.setUserName(self.username)
            self.loginObj.setPassword(self.password)
            self.loginObj.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            print('Title is: ', act_title)
            if act_title == 'Dashboard / nopCommerce administration':  # "Store Demo - nopCommerce":
                assert True
                self.logger.info("********** Verifying title after login Passed ******** ")
                self.driver.close()
            else:
                self.driver.save_screenshot(".\\Screenshots\\test_login.png")
                self.driver.close()
                self.logger.error('********** Verifying title after login failed ******** ')
                assert False
        except Exception:
            print("Exception here..............................")
