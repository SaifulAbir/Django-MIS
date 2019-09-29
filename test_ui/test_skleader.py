import time

from selenium.webdriver.ie.webdriver import WebDriver

from test_ui.config import *


def addSkleader(driver : WebDriver, data):
   driver.get(MAIN_URL + SKLEADER_URL)
   lnk_new_skleader = driver.find_element_by_link_text('New SK Leader')
   lnk_new_skleader.click()
   time.sleep(0.5)
   skleader_name = driver.find_element_by_name('UF-first_name')
   skleader_name.send_keys(data['NAME'])
   skleader_email = driver.find_element_by_name('UF-email')
   skleader_email.send_keys(data['MOBILE'] + '@sknf.org')
   skleader_mobile = driver.find_element_by_name('PF-mobile')
   skleader_mobile.send_keys(data['MOBILE'])
   skleader_class = driver.find_element_by_name('PF-student_class')
   skleader_class.send_keys(data['CLASS'])
   skleader_roll = driver.find_element_by_name('PF-roll')
   skleader_roll.send_keys('1')
   skleader_pass = driver.find_element_by_name('UF-password')
   skleader_pass.send_keys(data['MOBILE'])
   skleader_con_pass = driver.find_element_by_name('UF-confirm_password')
   skleader_con_pass.send_keys(data['MOBILE'])
   time.sleep(0.5)
   driver.find_element_by_class_name('select2-selection').click()
   search_box = driver.find_element_by_class_name('select2-search__field')
   search_box.send_keys(data['EIIN'])
   search_box.send_keys('\n')
   time.sleep(0.5)
   from_date = driver.find_element_by_class_name('datepicker')
   from_date.click()
   from_date.send_keys('01-09-2019')

   save_button = driver.find_element_by_xpath('/html/body/div/div[1]/form/section[2]/div[2]/div/div/div[2]/div[2]/input')
   save_button.click()
   # check that saved
   return 1