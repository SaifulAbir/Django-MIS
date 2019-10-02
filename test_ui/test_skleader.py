import time

from selenium.webdriver.ie.webdriver import WebDriver

from .config import *


def addSkleader(driver : WebDriver, data):
   driver.get(MAIN_URL + SKLEADER_URL)
   driver.find_element_by_link_text('New SK Leader').click()

   time.sleep(3)
   skleader_name = driver.find_element_by_name('UF-first_name')
   skleader_name.send_keys(data['NAME'])
   skleader_email = driver.find_element_by_name('UF-email')
   skleader_email.send_keys(data['MOBILE'] + '@sknf.org')
   skleader_mobile = driver.find_element_by_name('PF-mobile')
   skleader_mobile.send_keys(data['MOBILE'])
   skleader_class = driver.find_element_by_name('PF-student_class')
   skleader_class.send_keys(data['CLASS'])
   skleader_roll = driver.find_element_by_name('PF-roll')
   skleader_roll.send_keys('0')
   skleader_pass = driver.find_element_by_name('UF-password')
   skleader_pass.send_keys(data['MOBILE'])
   skleader_con_pass = driver.find_element_by_name('UF-confirm_password')
   skleader_con_pass.send_keys(data['MOBILE'])
   time.sleep(3)
   driver.find_element_by_class_name('select2-selection').click()
   search_box = driver.find_element_by_class_name('select2-search__field')
   search_box.send_keys(data['EIIN'])
   search_box.send_keys('\n')
   time.sleep(1)
   from_date = driver.find_element_by_class_name('datepicker')
   from_date.click()
   from_date.send_keys('01-09-2019')

   save_button = driver.find_element_by_id('save-btn')
   save_button.click()
   # check that saved
   return 1