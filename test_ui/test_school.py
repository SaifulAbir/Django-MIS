import time

from selenium.webdriver.support.select import Select


def addSchool(driver):
   school_name = driver.find_element_by_link_text('Schools')
   school_name.click()
   add_school = driver.find_element_by_link_text('New School')
   add_school.click()
   new_sc_name = driver.find_element_by_name('name')
   new_sc_name.send_keys('Niketon girls high school')
   school_id = driver.find_element_by_name('school_id')
   school_id.send_keys('nghs123456')
   school_address = driver.find_element_by_name('address')
   school_address.send_keys('Niketon')
   division_name = Select(driver.find_element_by_name('division'))
   division_name.select_by_index(4)
   time.sleep(2)
   district_name = Select(driver.find_element_by_name('district'))
   district_name.select_by_index(6)
   time.sleep(2)
   upazilla_name = Select(driver.find_element_by_name('upazilla'))
   upazilla_name.select_by_index(1)
   time.sleep(2)
   union_name = Select(driver.find_element_by_name('union'))
   union_name.select_by_index(1)
   time.sleep(2)
   save_button = driver.find_element_by_class_name('btn-primary')
   save_button.click()
