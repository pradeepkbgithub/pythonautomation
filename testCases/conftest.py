import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def setup1():
    # driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe") # drivers/chromedriver.exe
    # s = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=s)
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(options=options)

    # Use the `install()` method to set `executabe_path` in a new `Service` instance:
    service = Service(executable_path=ChromeDriverManager().install())
    # Pass in the `Service` instance with the `service` keyword:
    driver = webdriver.Chrome(service=service)

    driver.delete_all_cookies()
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    return driver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        # driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe") # drivers/chromedriver.exe
        # s = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=s)
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # driver = webdriver.Chrome(options=options)

        # Use the `install()` method to set `executabe_path` in a new `Service` instance:
        service = Service(executable_path=ChromeDriverManager().install())

        # Pass in the `Service` instance with the `service` keyword:
        driver = webdriver.Chrome(service=service)
        print('Launching Chrome browser................')
    elif browser == 'firefox':
        # driver=webdriver.Firefox();
        service = Service(Options.binary)

        driver = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
        print('Launching Firefox browser................')

    elif browser == 'ie':
        driver = webdriver.Ie(executable_path='drivers/IEDriverServer.exe')
        print('Launching IE browser................')

    elif browser == 'edge':
        driver = webdriver.Edge(executable_path='drivers/msedgedriver.exe')
        print('Launching EDGE browser................')
    else:  # default browser....
        # Use the `install()` method to set `executabe_path` in a new `Service` instance:
        service = Service(executable_path=ChromeDriverManager().install())
        # Pass in the `Service` instance with the `service` keyword:
        driver = webdriver.Chrome(service=service)

    driver.delete_all_cookies()
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    return driver


def pytest_addoption(parser):  # this will get value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")
