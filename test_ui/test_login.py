import time

from selenium.common.exceptions import NoSuchElementException


def login(driver, data):
   admin_name = driver.find_element_by_name('email')
   admin_name.clear()
   admin_name.send_keys(data['email'])
   admin_pass = driver.find_element_by_name('password')
   admin_pass.send_keys(data['password'])
   admin_pass.submit()
   time.sleep(1)
   try:
      driver.find_element_by_link_text(data['email'])
      return 1
   except NoSuchElementException:
      return 0



def logout(driver):
   profile_name = driver.find_element_by_class_name('dropdown-toggle')
   profile_name.click()

   sign_out = driver.find_element_by_link_text('Sign out')
   sign_out.click()
