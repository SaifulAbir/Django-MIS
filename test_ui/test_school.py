import time

import pandas as pd
from selenium.webdriver.support.select import Select


def addSchool(driver, data):
   school_name = driver.find_element_by_link_text('Schools')
   school_name.click()
   add_school = driver.find_element_by_link_text('New School')
   add_school.click()
   new_sc_name = driver.find_element_by_name('name')
   new_sc_name.send_keys(data['name'])
   if not pd.isna(data['eiin']):
      school_id = driver.find_element_by_name('school_id')
      school_id.send_keys(data['eiin'])
   if not pd.isna(data['address']):
      school_address = driver.find_element_by_name('address')
      school_address.send_keys(data['address'])
   # if not pd.isna(data['division']):
   #    division_name = Select(driver.find_element_by_name('division'))
   #    division_name.select_by_visible_text(data['division'])
   # if not pd.isna(data['district']):
   #    district_name = Select(driver.find_element_by_name('district'))
   #    district_name.select_by_visible_text()
   # if not pd.isna(data['upazilla']):
   #    upazilla_name = Select(driver.find_element_by_name('upazilla'))
   #    upazilla_name.select_by_visible_text()
   # if not pd.isna(data['union']):
   #    union_name = Select(driver.find_element_by_name('union'))
   #    union_name.select_by_visible_text()
   save_button = driver.find_element_by_class_name('btn-primary')
   save_button.click()
   return 1
