"""
Main file.
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

from credentials import USER_NAME, PASSWORD
from search_words import search_words

LOGIN_URL = 'https://login.live.com/'
REWARD_URL = 'https://rewards.bing.com/'

EMAIL_FIELD = (By.CSS_SELECTOR, 'input[aria-label="Enter your email, phone, or Skype."]')
PASSWORD_FIELD = (By.ID, 'passwordEntry')
NEXT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
DECLINE_BUTTON = (By.CSS_SELECTOR, 'data-testid="secondaryButton"')

# Edge is used with my own profile so let's use Chrome here.
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(LOGIN_URL)

# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAIL_FIELD)).send_keys(USER_NAME)

# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

# wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(PASSWORD)

# Click Login - same id?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

# Stay signed in?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(DECLINE_BUTTON)).click()


BING_URL = 'https://www.bing.com/'
SEARCH_BOX = (By.ID, "sb_form_q")
FIRST_NAME = (By.ID, "id_n")

browser.get(BING_URL)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(FIRST_NAME))

search_words = ['MLB ' + str(i) for i in range(1990, 2020)]
for word in search_words:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(SEARCH_BOX)).send_keys(word + "\n")
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(SEARCH_BOX)).clear()
    browser.implicitly_wait(10)

# while True:
#     pass
