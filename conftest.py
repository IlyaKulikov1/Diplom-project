import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--disable-gpu")
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.accept_untrusted_certs = True
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()
