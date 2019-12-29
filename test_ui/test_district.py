import time

from .config import *


def addDistrict(driver, data):
    try:
        driver.get(MAIN_URL + DISTRICT_URL)
        lnk_new_district = driver.find_element_by_class_name('js-create-district')
        lnk_new_district.click()
        time.sleep(DELAY_SHORT)
        division_name = driver.find_element_by_name('division')
        division_name.send_keys(data['DIVISION'])
        district_name = driver.find_element_by_name('name')
        district_name.send_keys(data['DISTRICT'])
        save_button = driver.find_element_by_id('districtSubmit')
        time.sleep(DELAY_SHORT)
        save_button.click()
        time.sleep(DELAY_SHORT)
        # check that saved
        driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
        return 1
    except Exception as ex:
        return 0
