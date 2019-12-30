import selenium.webdriver as webdriver
import contextlib
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException

from test_ui.fullScreen import fullScreenShot


@contextlib.contextmanager
def quitting(thing):
    yield thing
    thing.quit()


driver = webdriver.Chrome('driver/chromedriver')
def screenShot():

    driver.get('http://localhost:8000')
    driver.maximize_window()
    driver.find_elements_by_xpath("//*[contains(text(), 'Sign In')]")
    admin_name = driver.find_element_by_name('email')
    admin_name.clear()
    admin_name.send_keys('admin')
    admin_pass = driver.find_element_by_name('password')
    admin_pass.send_keys('123')
    admin_pass.submit()
    data = pd.read_csv("testdata/url.csv", dtype=str)
    for idx, row in data.iterrows():
        fullScreenShot(driver, row)

    # driver.get(row['PAGE'])
    # print(row['FILE_NAME'])
    # if row['FILE_NAME'] == 'School_Search':
    #     driver.find_element_by_id('advancedButton').click()
    #     time.sleep(2)
    # driver.implicitly_wait(2)
    # driver.find_element_by_tag_name('body')
    # #driver.get_screenshot_as_file('images/' + row['FILE_NAME'] + '.png')
    # driver.get_screenshot_as_file('images/' + row['FILE_NAME'] + '.png')

screenShot()
