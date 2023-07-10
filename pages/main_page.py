import time

import allure
from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from pages.locators import main_page_locators as mpl
from conftest import driver
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_main_page(self):
        with allure.step("go to main page"):
            self.driver.get('https://www.whitehouse.gov/')

    def check_header_links(self):

        xpaths = [mpl.header_administration, mpl.header_priorities,
                  mpl.header_the_record, mpl.header_briefing,
                  mpl.header_change_lng
                  ]

        for xpath in xpaths:
            link = self.find_element(xpath)
            with allure.step(f'Checking for displaying {link.text} and clicking on an element'):
                if self.is_element_visible(xpath):
                    link.click()
                    self.go_to_main_page()
                else:
                    print(f'Link {link.text} is not displayed')

    def open_search_field(self):
        with allure.step("opening search field"):
            if self.is_element_visible(mpl.search_icon):
                self.find_element(mpl.search_icon).click()

    def fill_search_field(self):
        with allure.step("filling search field"):
            self.find_element(mpl.search_field).send_keys("Remarks")
        with allure.step("Press to submit-button"):
            self.find_element(mpl.search_confirm).click()


