import allure
from pages.main_page import MainPage
from pages.search_result_page import SearchResult
from pages.past_presidents_page import PastPresidents
from pages.kennedy_page import KennedyPage
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


@allure.suite("Past Presidents")
@allure.title("clicking on card and checking inconsistencies in the text")
def test_kennedy_card(driver):
    past_president_page = PastPresidents(driver)
    past_president_page.open_past_presidents_page()
    past_president_page.open_kennedy_card_with_js()
    kennedy_page = KennedyPage(driver)
    assert kennedy_page.expected_result() == kennedy_page.additional_result(), 'Inconsistencies in the text'


@allure.suite("toggle buttons")
@allure.title("clicking on buttons")
def test_toggle_buttons(driver):
    """123"""
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.click_on_high_contrast()
    main_page.click_on_large_fonts()
    assert MainPage.hight_contrast_result(driver) == 'acctoggle__contrast active', '!!!!!!!!!!!!!!!!!!!'
    assert MainPage.large_fonts_result(driver) == 'acctoggle__fontsize active', '!!!!!!!!!!!!!!!!!!!!!'