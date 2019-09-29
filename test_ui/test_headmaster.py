import time

from selenium.webdriver.ie.webdriver import WebDriver

from test_ui.config import *


def addHeadmaster(driver : WebDriver, data):
   driver.get(MAIN_URL + HEADMASTER_URL)
   lnk_new_headmaster = driver.find_element_by_link_text('New Headmaster')
   lnk_new_headmaster.click()
   time.sleep(0.5)
   headmaster_name = driver.find_element_by_name('UF-first_name')
   headmaster_name.send_keys(data['NAME'])
   headmaster_email = driver.find_element_by_name('UF-email')
   headmaster_email.send_keys(data['MOBILE'] + '@sknf.org')
   headmaster_mobile = driver.find_element_by_name('PF-mobile')
   headmaster_mobile.send_keys(data['MOBILE'])
   headmaster_pass = driver.find_element_by_name('UF-password')
   headmaster_pass.send_keys(data['MOBILE'])
   headmaster_con_pass = driver.find_element_by_name('UF-confirm_password')
   headmaster_con_pass.send_keys(data['MOBILE'])
   user_type = driver.find_element_by_id('id_UF-user_type_0')
   user_type.click()
   time.sleep(0.5)
   driver.find_element_by_class_name('select2-selection').click()
   search_box = driver.find_element_by_class_name('select2-search__field')
   search_box.send_keys(data['EIIN'])
   search_box.send_keys('\n')
   time.sleep(0.5)
   from_date = driver.find_element_by_class_name('datepicker')
   from_date.click()
   from_date.send_keys('01-09-2019')

   save_button = driver.find_element_by_xpath('/html/body/div/div[1]/form/section[2]/div[3]/div/div/input')
   save_button.click()
   # check that saved
   return 1