import time

from.config import *

def addDivision(driver, data):
   driver.get(MAIN_URL + DIVISION_URL)
   lnk_new_division = driver.find_element_by_class_name('js-create-division')
   lnk_new_division.click()
   time.sleep(DELAY_SHORT)
   division_name = driver.find_element_by_name('name')
   division_name.send_keys(data['DIVISION'])
   save_button = driver.find_element_by_id('id_username')
   save_button.click()
   # check that saved
   return 1
