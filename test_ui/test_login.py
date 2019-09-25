import time

from selenium.webdriver.support.select import Select


def login(driver):
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
