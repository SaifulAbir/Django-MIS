import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

from test_ui.config import MAIN_URL

driver = webdriver.Chrome('driver/chromedriver')
driver.get(MAIN_URL)
time.sleep(2)

def login():
   users = ['', 'rashad', 'shohag', 'rashed', 'rashed','admin']
   psswords = ['', 'abc123', '123456', 'mahadi', '123456','123']
   for i in range(len(users)):
       admin_name = driver.find_element_by_name('email')
       admin_name.clear()
       admin_name.send_keys(users[i])
       admin_pass = driver.find_element_by_name('password')
       admin_pass.send_keys(psswords[i])
       admin_pass.submit()
       time.sleep(5)

def addSchool():
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
login()
addSchool()
time.sleep(5)
driver.quit()