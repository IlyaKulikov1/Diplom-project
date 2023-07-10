from selenium.webdriver.common.by import By

link_main_page = 'https://www.whitehouse.gov/'

# Header buttons's Xpath-s

header_logo = (By.XPATH, '//*[@class="desktop__logo"]')

header_icon_logo = (By.XPATH, '//*[@id="wh-oval-697"]')

header_administration = (By.XPATH, "//*[@id='menu-item-61']")

header_priorities = (By.XPATH, "//*[@id='menu-item-64']")

header_the_record = (By.XPATH, "//*[@id='menu-item-65469']")

header_briefing  = (By.XPATH, "//*[@id='menu-item-2787']")

header_change_lng = (By.XPATH, "//*[@id='menu-item-199']")

header_menu = (By.XPATH, "//*[@id='mm-label']")

# button high contrast not active
btn_high_contrast = (By.XPATH, '//*[@class="acctoggle__contrast"]')

# button Toggle Large Font Size not active
btn_font_size = (By.XPATH, '//*[@class="acctoggle__fontsize"]')

# Past Presidents
btn_past_presidents = (By.XPATH, "//*[@class='homepage-about-menu-item']//*[text()='Past Presidents']")

# Search field
search_icon = (By.XPATH, '//section[@class="homepage-taskbar homepage-taskbar--js"]//button[@class="search-icon"]')

search_field = (By.XPATH, '(//*[@class="search-field"])[2]')

search_confirm = (By.XPATH, '(//*[@class="search-submit"])[2]')

