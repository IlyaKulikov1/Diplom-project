import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import main_page_locators
from selenium.common import TimeoutException


class BasePage:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

# return current url
    def get_current_url(self):

        return self.driver.current_url

    def find_element(self, *args):
        """ Метод find_element() принимает два аргумента:
            by_name и by_val, которые определяют, как искать
            элемент на странице. Метод использует self.driver
            для поиска элемента на странице и возвращает найденный элемент"""

        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def is_element_visible(self, *args):
        """ Метод is_element_visible() также принимает два аргумента:
            by_name и by_val, которые определяют, как искать элемент на странице.
            Метод использует WebDriverWait для ожидания видимости
            элемента на странице в течение 10 секунд, после чего
            он возвращает найденный элемент. Если элемент не появляется
            на странице в течение 10 секунд, возникает исключение TimeoutException"""

        by_name, by_val = args[0]
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by_name, by_val))
        )
        return self.driver.find_element(by_name, by_val)

    def is_not_element_present(self, *args):
        """ Метод is_not_element_present() проверяет, что элемент не появляется
            на странице в течение 10 секунд. Метод принимает два аргумента:
            by_name и by_val, которые определяют, как искать элемент на странице.
            Метод использует WebDriverWait для ожидания отсутствия элемента на
            странице в течение 10 секунд. Если элемент не появляется на
            странице в течение 10 секунд, метод возвращает True. Если элемент
            все же появляется, возникает исключение TimeoutException, и метод возвращает False"""

        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def is_element_present(self, *args):
        """ Метод is_element_present() проверяет, что элемент появляется
            на странице в течение 10 секунд. Метод принимает два аргумента:
            by_name и by_val, которые определяют, как искать элемент
            на странице. Метод использует WebDriverWait для ожидания
            появления элемента на странице в течение 10 секунд. Если элемент
            появляется на странице в течение 10 секунд, метод возвращает True.
            Если элемент не появляется, возникает исключение TimeoutException,
            и метод возвращает False"""

        try:
            by_name, by_val = args[0]
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by_name, by_val)),
            )
        except TimeoutException:
            return False
        return True

    def find_elements(self, *args):
        """ Метод find_elements() находит все элементы на странице,
            соответствующие заданным параметрам поиска. Метод принимает
            два аргумента: by_name и by_val, которые определяют,
            как искать элементы на странице. Метод использует self.driver
            для поиска элементов на странице и возвращает найденные элементы"""

        by_name, by_val = args[0]
        return self.driver.find_elements(by_name, by_val)

    def go_to_main_page(self):
        """ Метод go_to_main_page() переходит на главную страницу.
            Метод использует метод is_element_visible() для поиска
            элемента с логотипом на странице и кликает на него.
            Метод is_element_visible() ожидает, что элемент с
            логотипом появится на странице и станет видимым в течение 10 секунд.
            Если элемент не появляется на странице в течение 10 секунд,
            возникает исключение TimeoutException"""

        self.is_element_visible(main_page_locators.header_logo).click()