import time

import pytest

from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.loginObj = LoginPage(self.driver)
        self.loginObj.setUserName(self.username)
        self.loginObj.setPassword(self.password)
        self.loginObj.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcustObj = AddCustomerPage(self.driver)
        self.addcustObj.clickOnCustomersMenu()
        self.addcustObj.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchcustObj = SearchCustomerPage(self.driver)
        searchcustObj.setEmail("victoria_victoria@nopCommerce.com")
        searchcustObj.clickSearch()
        time.sleep(5)
        status = searchcustObj.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
