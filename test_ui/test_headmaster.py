import time

from selenium.webdriver.ie.webdriver import WebDriver

from test_ui.config import *


def addHeadmaster(driver : WebDriver, data):
   driver.get(MAIN_URL + HEADMASTER_URL)
   lnk_new_headmaster = driver.find_element_by_link_text('New Headmaster')
   lnk_new_headmaster.click()
   time.sleep(0.5)
   headmaster_name = driver.find_element_by_name('UF-first_name')
   headmaster_name.send_keys(data['name'])
   headmaster_email = driver.find_element_by_name('UF-email')
   headmaster_email.send_keys(data['mobile'] + '@sknf.org')
   headmaster_mobile = driver.find_element_by_name('PF-mobile')
   headmaster_mobile.send_keys(data['mobile'])
   headmaster_pass = driver.find_element_by_name('UF-password')
   headmaster_pass.send_keys(data['mobile'])
   headmaster_con_pass = driver.find_element_by_name('UF-confirm_password')
   headmaster_con_pass.send_keys(data['mobile'])
   user_type = driver.find_element_by_id('id_UF-user_type_0')
   user_type.click()
   headmaster_school_name = driver.find_element_by_name('PF-school')
   headmaster_school_name.send_keys(data['school'])
   from_date = driver.find_element_by_class_name('datepicker')
   from_date.click()
   from_date.send_keys('28-09-2019')

   save_button = driver.find_element_by_xpath('/html/body/div/div[1]/form/section[2]/div[3]/div/div/input')
   save_button.click()
   # check that saved
   return 1