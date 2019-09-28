import time

from test_ui.config import *


def addDistrict(driver, data):
   driver.get(MAIN_URL + DISTRICT_URL)
   lnk_new_district = driver.find_element_by_class_name('js-create-district')
   lnk_new_district.click()
   time.sleep(0.5)
   division_name = driver.find_element_by_name('division')
   division_name.send_keys(data['division'])
   district_name = driver.find_element_by_name('name')
   district_name.send_keys(data['district'])
   save_button = driver.find_element_by_id('id_username')
   save_button.click()
   # check that saved
   return 1
