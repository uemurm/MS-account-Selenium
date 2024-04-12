'''
Main file.
'''
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

from credentials import USER_NAME, PASSWORD

LOGIN_URL = 'https://login.live.com/'
REWARD_URL = 'https://rewards.bing.com/'

EMAILFIELD = (By.ID, "i0116")
PASSWORD_FIELD = (By.ID, "i0118")
NEXT_BUTTON = (By.ID, "idSIButton9")
DECLINE_BUTTON = (By.ID, "declineButton")

browser = webdriver.Chrome()
browser.get(REWARD_URL)

# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(USER_NAME)

# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

# wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORD_FIELD)).send_keys(PASSWORD)

# Click Login - same id?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

# Stay signed in?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(DECLINE_BUTTON)).click()
