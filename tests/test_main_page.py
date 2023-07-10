import allure
# from pages.locators import main_page_locators
# from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.search_result_page import SearchResult
from conftest import driver



@allure.suite("Header links")
@allure.title("Checking for displaying and clicking on header's elements")
def test_header(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.check_header_links()


@allure.suite("Search field")
@allure.title("filling in the search field")
def test_search_field(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.open_search_field()
    main_page.fill_search_field()
    search_results_page = SearchResult(driver)
    assert search_results_page.check_for_search_results(), "Error with search result"

