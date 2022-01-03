import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.get_application_url()  # "https://www.nopcommerce.com/en/login"
    path = ReadConfig.getTestDataPath()

    username = ReadConfig.get_user_email()  # "test"
    password = ReadConfig.get_password()  # "test"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info('********** Test_002_DDT_Login ******************')
        self.logger.info('********** Verifying login test_login_ddt ******')
        try:
            self.driver = setup  # webdriver.chrome()
            self.driver.get(self.baseURL)
            time.sleep(10)
            self.loginObj = LoginPage(self.driver)

            self.rows = XLUtils.getRowCount(self.path, 'UserLogin')
            print('Number of Rows in a Excel: ', self.rows)

            list_status = []

            for r in range(2, self.rows + 1):
                self.user = XLUtils.readData(self.path, 'UserLogin', r, 1)
                self.password = XLUtils.readData(self.path, 'UserLogin', r, 2)
                self.exp = XLUtils.readData(self.path, 'UserLogin', r, 3)

                print('Row Data--> ',self.user, '  ',self.password,' ',self.exp)
                #self.loginObj.clickUserLink()
                #self.loginObj.clickLoginLink()

                self.loginObj.setUserName(self.user)
                self.loginObj.setPassword(self.password)
                self.loginObj.clickLogin()
                time.sleep(5)

                act_title = self.driver.title
                print('Title is: ', act_title)
                exp_title = "Dashboard / nopCommerce administration"

                if act_title == exp_title:
                    if self.exp == 'Pass':
                        self.logger.info("***** Test Pass")
                        #self.loginObj.clickUserLink()
                        time.sleep(3)
                        self.loginObj.clickLogout()
                        list_status.append('Pass')
                    elif self.exp == 'Fail':
                        self.logger.info("***** Test Failed")
                        #self.loginObj.clickUserLink()
                        time.sleep(3)
                        self.loginObj.clickLogout()
                        list_status.append('Fail')
                elif act_title != exp_title:
                    if self.exp == 'Pass':
                        self.logger.info("***** Test Failed")
                        list_status.append('Fail')
                    elif self.exp == 'Fail':
                        self.logger.info("***** Test Pass")
                        list_status.append('Pass')

            print('list********************: ', list_status)
            if 'Fail' not in list_status and self.rows-1 == len(list_status):
                print("PA=========================================================")
                self.logger.info('Login DDT test passed...')
                self.driver.close()
                assert True
            else:
                self.logger.info('Login DDT test failed...')
                self.driver.close()
                assert False
        except BaseException:
            print("Exception here..............................")
            print('list********************: ', list_status)
            assert False

        self.logger.info('***** End of Login DDT Test ****')
        self.logger.info('***** Completed Test_002_DDT_Login **')
