import allure
from pages.base_page import BasePage
from pages.locators import main_page_locators as mpl
from pages.locators import search_result_locators as srl


class SearchResult(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_for_search_results(self):
        with allure.step("Checking number of result's elements"):
            if len(self.find_elements(srl.search_results)) >= 1:
                return True
