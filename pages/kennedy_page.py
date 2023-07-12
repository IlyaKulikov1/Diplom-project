import time

import allure
from pages.base_page import BasePage
from pages.locators import Kennedy_locators as kl


class KennedyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def expected_result(self):
        return "John F. Kennedy was the 35th President of the United States (1961-1963)," \
               " the youngest man elected to the office. On November 22, 1963, when he was" \
               " hardly past his first thousand days in office, JFK was assassinated in Dallas, Texas," \
               " becoming also the youngest President to die."

    def additional_result(self):
        return self.find_element(kl.kennedy_info).text

