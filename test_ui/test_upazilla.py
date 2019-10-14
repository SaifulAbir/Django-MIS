import time

from test_ui.config import *


def addUpazilla(driver, data):
   driver.get(MAIN_URL + UPAZILLA_URL)
   lnk_new_upazilla = driver.find_element_by_class_name('js-create-upazilla')
   lnk_new_upazilla.click()
   time.sleep(0.5)
   division_name = driver.find_element_by_name('division')
   division_name.send_keys(data['DIVISION'])
   district_name = driver.find_element_by_name('district')
   district_name.send_keys(data['DISTRICT'])
   upazilla_name = driver.find_element_by_name('name')
   upazilla_name.send_keys(data['UPAZILA'])
   save_button = driver.find_element_by_id('id_username')
   save_button.click()
   # check that saved
   return 1