import time

from.config import *


def addUnion(driver, data):
   try:
      driver.get(MAIN_URL + UNION_URL)
      lnk_new_upazilla = driver.find_element_by_class_name('js-create-union')
      lnk_new_upazilla.click()
      time.sleep(4)
      division_name = driver.find_element_by_name('division')
      division_name.send_keys(data['DIVISION'])
      time.sleep(3)
      district_name = driver.find_element_by_name('district')
      district_name.send_keys(data['DISTRICT'])
      upazilla_name = driver.find_element_by_name('upazilla')
      upazilla_name.send_keys(data['UPAZILA'])
      upazilla_name = driver.find_element_by_name('name')
      upazilla_name.send_keys(data['UNION'])
      save_button = driver.find_element_by_id('unionSubmit')
      save_button.click()
      time.sleep(DELAY_SHORT)
      # check that saved
      driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
      return 1
   except Exception as ex:
      return 0