import requests, allure
from pages.Api.api_page import Urls, Headers


def test_wh_outline():

  response = requests.request("GET", Urls.url_outline_img, headers=Headers.headers_outline_img)
  with allure.step('Checking for status code 200'):
    assert response.status_code == 200

def test_footer_seal():

  response = requests.request("GET", Urls.url_footer_seal, headers=Headers.headers_footer_seal)
  with allure.step('Checking for status code 200'):
    assert response.status_code == 200
