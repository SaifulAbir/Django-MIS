import time

import pandas as pd
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from.config import *

def addSchool(driver : WebDriver, data):
   driver.get(MAIN_URL + SCHOOL_URL)
   add_school = driver.find_element_by_link_text('New School')
   add_school.click()
   time.sleep(4)
   new_sc_name = driver.find_element_by_name('name')
   new_sc_name.send_keys(data['SCHOOL'])
   if not pd.isna(data['EIIN']):
      school_id = driver.find_element_by_name('school_id')
      school_id.send_keys(data['EIIN'])

   if not pd.isna(data['UPAZILA']):
      school_address = driver.find_element_by_name('address')
      school_address.send_keys(data['UPAZILA'])
   time.sleep(4)
   if not pd.isna(data['DIVISION']):
      division_name = Select(driver.find_element_by_name('division'))
      division_name.select_by_visible_text(data['DIVISION'])
   time.sleep(4)
   if not pd.isna(data['DISTRICT']):
      district_name = Select(driver.find_element_by_name('district'))
      district_name.select_by_visible_text(data['DISTRICT'])
   time.sleep(4)
   if not pd.isna(data['UPAZILA']):
      upazilla_name = Select(driver.find_element_by_name('upazilla'))
      upazilla_name.select_by_visible_text(data['UPAZILA'])
   time.sleep(1)
   if not pd.isna(data['UNION']):
      union_name = Select(driver.find_element_by_name('union'))
      union_name.select_by_visible_text(data['UNION'])
   save_button = driver.find_element_by_id('save-btn')
   save_button.click()
   return 1
