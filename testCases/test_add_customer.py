import string
import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.LoginPage import LoginPage
from utilities.customeLogger import LogGen
from utilities.readProperties import ReadConfig
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.get_application_url()  # "https://www.nopcommerce.com/en/login"
    username = ReadConfig.get_user_email()  # "test"
    password = ReadConfig.get_password()  # "test"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCutomer(self, setup):
        try:
            self.logger.info("************ Test_003_AddCustomer *******")
            self.driver = setup  # webdriver.chrome()
            self.driver.get(self.baseURL)
            act_title = self.driver.title
            print("===================== " + act_title)

            self.loginObj = LoginPage(self.driver)
            self.loginObj.setUserName(self.username)
            self.loginObj.setPassword(self.password)
            self.loginObj.clickLogin()
            time.sleep(5)

            self.logger.info("********* Login Successful *********")

            self.logger.info("**** Starting Add Customer Test ****")

            self.addCustObj = AddCustomerPage(self.driver)
            self.addCustObj.clickOnCustomersMenu()
            self.addCustObj.clickOnCustomersMenuItem()

            self.addCustObj.clickOnAddnew()
            time.sleep(5)

            self.logger.info("*****Providing Customer Information******")

            self.email = random_generator() + "sp2021@gmail.com"
            print("Your email id: ", self.email)
            self.addCustObj.setEmail(self.email)
            self.addCustObj.setPassword("test123")
            self.addCustObj.setFirstName("Test")
            self.addCustObj.setLastName("Selenium")
            self.addCustObj.setGender("Male")
            self.addCustObj.setDob("7/05/1985")  # Format: D / MM / YYY
            self.addCustObj.setCompanyName("SeleniumQA")

            self.addCustObj.setCustomerRoles("Guests")
            self.addCustObj.setManagerOfVendor("Vendor 2")
            self.addCustObj.setAdminContent("This is for testing selenium.........")
            self.addCustObj.clickOnSave()
            time.sleep(5)
            self.logger.info("************* Saving customer info **********")

            self.logger.info("********* Add customer validation started *****************")

            self.msg = self.driver.find_element(By.TAG_NAME, "body").text

            print("Message=======>: ", self.msg)
            if 'customer has been added successfully.' in self.msg:
                assert True
                self.logger.info("********* Add customer Test Passed *************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
                self.logger.error("********* Add customer Test Failed ************")
                assert False

            self.driver.close()
            self.logger.info("******* Ending Add customer test **********")

        except BaseException:
            print("Adding customer exception*********************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
