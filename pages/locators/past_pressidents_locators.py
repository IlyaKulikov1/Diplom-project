from selenium.webdriver.common.by import By

# Card of 35th Presideent
kennedy_card = (By.XPATH, "//*[contains(text(),'John F. Kennedy')]")

#js script for clicking

kennedy_card_script = """document.querySelector('a[href="https://www.whitehouse.gov/about-the-white-house/presidents/john-f-kennedy/"]').click()"""
