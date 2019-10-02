import time

import pandas as pd
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from.config import *

def addSkmember(driver : WebDriver, data):
   driver.get(MAIN_URL + SKMEMBER_URL)
   driver.find_element_by_link_text('New SK Member').click()

   time.sleep(DELAY_SHORT)
   driver.find_element_by_class_name('select2-selection__rendered').click()
   search_box = driver.find_element_by_class_name('select2-search__field')
   search_box.send_keys(data['EIIN'])
   search_box.send_keys('\n')
   skmember_name = driver.find_element_by_name('UF-first_name')
   skmember_name.send_keys(data['NAME'])
   skmember_email = driver.find_element_by_name('UF-email')
   skmember_email.send_keys(data['MOBILE'] + '@sknf.org')
   skmember_mobile = driver.find_element_by_name('PF-mobile')
   skmember_mobile.send_keys(data['MOBILE'])
   skmember_class = driver.find_element_by_name('PF-student_class')
   skmember_class.send_keys(data['CLASS'])
   skmember_roll = driver.find_element_by_name('PF-roll')
   skmember_roll.send_keys('1')

   save_button = driver.find_element_by_id('save-btn')
   save_button.click()
   # check that saved
   return 1


