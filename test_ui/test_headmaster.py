import time
from datetime import date

import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.ie.webdriver import WebDriver

from .config import *


def addHeadmaster(driver: WebDriver, data):
    driver.get(MAIN_URL + HEADMASTER_URL)
    lnk_new_headmaster = driver.find_element_by_link_text('New Headmaster')
    lnk_new_headmaster.click()
    time.sleep(DELAY_SHORT)
    time.sleep(1)
    try:
        headmaster_name = driver.find_element_by_name('UF-first_name')
        headmaster_name.send_keys(data['_name'])
        headmaster_email = driver.find_element_by_name('UF-email')
        headmaster_email.send_keys(data['_mobile'])
        headmaster_mobile = driver.find_element_by_name('PF-mobile')
        headmaster_mobile.send_keys(data['_mobile'])
        time.sleep(1)
        headmaster_pass = driver.find_element_by_name('UF-password')
        headmaster_pass.send_keys('123')
        # headmaster_pass.send_keys(data['_password'])
        time.sleep(1)
        headmaster_con_pass = driver.find_element_by_name('UF-confirm_password')
        headmaster_con_pass.send_keys('123')
        # headmaster_con_pass.send_keys(data['_con_password'])
        # time.sleep(1)
        # user_type = driver.find_element_by_id('id_UF-user_type_'+data['_user_type'])
        # user_type.click()
        time.sleep(1)
        driver.find_element_by_class_name('select2-selection').click()
        search_box = driver.find_element_by_class_name('select2-search__field')
        search_box.send_keys(data['_eiin'])
        search_box.send_keys('\n')
        time.sleep(1)

        from_date = driver.find_element_by_class_name('datepicker')
        from_date.click()
        from_date.send_keys('24-12-2019')
        # from_date.send_keys(data["_from_date"])
        time.sleep(5)
        save_button = driver.find_element_by_id('save-btn')
        save_button.click()
        # check that saved
        #driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
        driver.find_element_by_link_text('New Headmaster')
        return 1
    except Exception as ex:
        return 0


def updateHeadmaster(driver: WebDriver, data):
    driver.get(MAIN_URL + HEADMASTER_URL)
    time.sleep(3)
    try:
        search_box_name = driver.find_element_by_name('name_contains')
        search_box_name.send_keys(data['_name'])
        time.sleep(1)
        search_box__school = driver.find_element_by_name('school_contains')
        search_box__school.send_keys(data['_school'])
        search_button = driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[2]/button')
        search_button.click()
        edit_headmaster = driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr[1]/td[5]/a[2]/span')
        time.sleep(1)
        edit_headmaster.click()

        if not pd.isna(data['_name']):
            headmaster_name = driver.find_element_by_name('first_name')
            headmaster_name.clear()
            time.sleep(1)
            headmaster_name.send_keys(data['_name'])
        if not pd.isna(data['_email']):
            headmaster_email = driver.find_element_by_name('email')
            headmaster_email.clear()
            time.sleep(1)
            headmaster_email.send_keys(data['_email'])
        if not pd.isna(data['_mobile']):
            headmaster_mobile = driver.find_element_by_name('mobile')
            headmaster_mobile.clear()
            time.sleep(1)
            headmaster_mobile.send_keys(data['_mobile'])
        if not pd.isna(data['_password']):
            headmaster_pass = driver.find_element_by_name('password')
            headmaster_pass.clear()
            time.sleep(1)
            headmaster_pass.send_keys(data['_password'])
        if not pd.isna(data['_con_password']):
            headmaster_con_pass = driver.find_element_by_name('confirm_password')
            headmaster_con_pass.clear()
            time.sleep(1)
            headmaster_con_pass.send_keys(data['_con_password'])
        if not pd.isna(data['_user_type']):
            user_type = driver.find_element_by_id('id_UF-user_type_' + data['_user_type'])
            user_type.click()

        time.sleep(3)

        # if not pd.isna(data['TO_DATE']):
        #     time.sleep(3)
        #     to_date = driver.find_elements_by_xpath("//*[contains(@name, 'to_date[]') and [contains(@value, '')]]")
        #     to_date.click()
        #     to_date.send_keys(data['TO_DATE'])
        #     if not pd.isna(data['NEW_EIIN']):
        #         driver.find_element_by_id('addMoreDoc').click()
        #         search_box = driver.find_element_by_xpath("//span[@class='select2-selection__rendered' and text()='---------']").click()
        #         search_box.send_keys(data['NEW_EIIN'])
        #         search_box.send_keys('\n')
        #         time.sleep(1)
        #         from_date = driver.find_element_by_xpath("//span[@name='from_date' and text()='']")
        #         from_date.click()
        #         from_date.send_keys(data['FROM_DATE'])
        #     update_2 = driver.find_element_by_xpath('/html/body/div/div[1]/form/section[2]/div[2]/div/div/div[2]/div/div[2]/input')
        #     update_2.click()
        # else:
        update_1 = driver.find_element_by_xpath('/html/body/div/div[1]/form/section[2]/div[1]/div/div/div[4]/div/div/input')
        update_1.click()
        # check that saved
        #driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
        driver.find_elements_by_class_name('alert alert-success-customized')
        return 1
    except Exception as ex:
        print(ex)
        return 0