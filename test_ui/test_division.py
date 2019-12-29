import time

from .config import *


def addDivision(driver, data):
    try:
        driver.get(MAIN_URL + DIVISION_URL)
        lnk_new_division = driver.find_element_by_class_name('js-create-division')
        lnk_new_division.click()
        time.sleep(DELAY_SHORT)
        division_name = driver.find_element_by_name('name')
        division_name.send_keys(data['_division'])
        save_button = driver.find_element_by_id('divisionSubmit')
        save_button.click()
        time.sleep(DELAY_SHORT)
        # check that saved
        driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
        return 1
    except Exception as ex:
        return 0
