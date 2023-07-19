import time

import allure
from pages.base_page import BasePage
from pages.locators import past_pressidents_locators as ppl


class PastPresidents(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_past_presidents_page(self):
        with allure.step("go to past presidents page"):
            self.driver.get('https://www.whitehouse.gov/about-the-white-house/presidents/')

    def open_kennedy_card(self):
        with allure.step("Open Kennedy card"):
            if self.is_element_visible(ppl.kennedy_card):
                time.sleep(2)
                self.find_element(ppl.kennedy_card).click()

    def open_kennedy_card_with_js(self):
        time.sleep(2)
        with allure.step('Open Kennedy card'):
            if self.is_element_visible(ppl.kennedy_card):
               self.driver.execute_script(ppl.kennedy_card_script)