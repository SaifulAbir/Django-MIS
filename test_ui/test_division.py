import time

from test_ui.config import *

def addDivision(driver, data):
   driver.get(MAIN_URL + DIVISION_URL)
   lnk_new_division = driver.find_element_by_class_name('js-create-division')
   lnk_new_division.click()
   time.sleep(0.5)
   division_name = driver.find_element_by_name('name')
   division_name.send_keys(data['name'])
   save_button = driver.find_element_by_id('id_username')
   save_button.click()
   # check that saved
   return 1
