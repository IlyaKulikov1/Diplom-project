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
                    raise Exception("Visability error")

    def open_search_field(self):
        with allure.step("opening search field"):
            if self.is_element_visible(mpl.search_icon):
                self.find_element(mpl.search_icon).click()

    def fill_search_field(self):
        with allure.step("filling search field"):
            self.find_element(mpl.search_field).send_keys("Remarks")
        with allure.step("Press to submit-button"):
            self.find_element(mpl.search_confirm).click()

    def click_on_high_contrast(self):
        if self.is_element_visible(mpl.btn_high_contrast_not_active):
            self.find_element(mpl.btn_high_contrast_not_active).click()

    def click_on_large_fonts(self):
        if self.is_element_visible(mpl.btn_font_size_not_active):
            self.find_element(mpl.btn_font_size_not_active).click()

    def hight_contrast_result(self):
        return BasePage.get_attr(self, mpl.btn_high_contrast_active_class)

    def large_fonts_result(self):
        return BasePage.get_attr(self, mpl.btn_font_size_active_class)