"""
Main file.
"""
import random
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

from credentials import USER_NAME, PASSWORD

SEARCH_INTERVAL_RANGE = (5, 10)

LOGIN_URL = 'https://login.live.com/'
REWARD_URL = 'https://rewards.bing.com/'

EMAIL_FIELD = (By.CSS_SELECTOR, 'input[type="email"]')
PASSWORD_FIELD = (By.ID, 'passwordEntry')
NEXT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
DECLINE_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="secondaryButton"]')

# Edge is used with my own profile so let's use Chrome here.
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(LOGIN_URL)

wait = WebDriverWait(browser, 5)

# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

wait.until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

# Password field
wait.until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(PASSWORD)
wait.until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

# Stay signed in?
wait.until(EC.element_to_be_clickable(DECLINE_BUTTON)).click()

#
# Bing page
#
BING_URL = 'https://www.bing.com/'
SEARCH_BOX = (By.ID, "sb_form_q")
FIRST_NAME = (By.ID, "id_n")

browser.get(BING_URL)
wait.until(EC.element_to_be_clickable(FIRST_NAME))

search_words = ['MLB ' + str(i) for i in range(1990, 2020)]
for word in search_words:
    wait.until(EC.element_to_be_clickable(SEARCH_BOX)).clear()
    wait.until(EC.element_to_be_clickable(SEARCH_BOX)).send_keys(word + "\n")

    time.sleep(random.uniform(*SEARCH_INTERVAL_RANGE))

while True:
    pass
