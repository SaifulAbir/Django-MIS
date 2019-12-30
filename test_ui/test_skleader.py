import os
import time

import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.ie.webdriver import WebDriver

from .config import *

def addSkleaderEntry(driver: WebDriver, data):
    driver.get(MAIN_URL + SKLEADER_URL)
    driver.find_element_by_link_text('New SK Leader').click()

    time.sleep(3)
    try:
        skleader_name = driver.find_element_by_name('UF-first_name')
        skleader_name.send_keys(data['NAME'])
        skleader_email = driver.find_element_by_name('UF-email')
        skleader_email.send_keys(data['MOBILE'])
        skleader_mobile = driver.find_element_by_name('PF-mobile')
        skleader_mobile.send_keys(data['MOBILE'])
        skleader_class = driver.find_element_by_name('PF-student_class')
        skleader_class.send_keys(data['CLASS'])
        skleader_roll = driver.find_element_by_name('PF-roll')
        skleader_roll.send_keys('0')
        skleader_gender = driver.find_element_by_name('PF-gender')
        skleader_gender.send_keys('Male')
        skleader_pass = driver.find_element_by_name('UF-password')
        skleader_pass.send_keys(data['MOBILE'])
        skleader_con_pass = driver.find_element_by_name('UF-confirm_password')
        skleader_con_pass.send_keys(data['MOBILE'])
        time.sleep(3)
        driver.find_element_by_class_name('select2-selection').click()
        search_box = driver.find_element_by_class_name('select2-search__field')
        search_box.send_keys(data['EIIN'])
        search_box.send_keys('\n')
        time.sleep(1)
        from_date = driver.find_element_by_class_name('datepicker')
        from_date.click()
        from_date.send_keys('01-10-2010')
        time.sleep(1)
        save_button = driver.find_element_by_id('save-btn')
        save_button.click()
        # check that saved

        #driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
        driver.find_element_by_class_name('alert alert-success-customized')
        return 1
    except Exception as ex:
        return 0



def addSkleader(driver: WebDriver, data):
    driver.get(MAIN_URL + SKLEADER_URL)
    driver.find_element_by_link_text('New SK Leader').click()

    time.sleep(3)
    try:
        skleader_name = driver.find_element_by_name('UF-first_name')
        skleader_name.send_keys(data['_name'])
        skleader_email = driver.find_element_by_name('UF-email')
        skleader_email.clear()
        skleader_email.send_keys(data['_email'])
        skleader_mobile = driver.find_element_by_name('PF-mobile')
        skleader_mobile.send_keys(data['_mobile'])
        skleader_class = driver.find_element_by_name('PF-student_class')
        skleader_class.send_keys(data['_class'])
        skleader_roll = driver.find_element_by_name('PF-roll')
        skleader_roll.send_keys(data['_roll'])
        skleader_gender = driver.find_element_by_name('PF-gender')
        skleader_gender.send_keys(data['_gender'])
        skleader_pass = driver.find_element_by_name('UF-password')
        skleader_pass.clear()
        skleader_pass.send_keys(data['_password'])
        skleader_con_pass = driver.find_element_by_name('UF-confirm_password')
        skleader_con_pass.send_keys(data['_con_password'])
        time.sleep(3)
        driver.find_element_by_class_name('select2-selection').click()
        search_box = driver.find_element_by_class_name('select2-search__field')
        search_box.send_keys(data['_eiin'])
        search_box.send_keys('\n')
        time.sleep(1)
        from_date = driver.find_element_by_class_name('datepicker')
        from_date.click()
        from_date.send_keys(data['_from_date'])
        save_button = driver.find_element_by_id('save-btn')
        save_button.click()
        # check that saved

        driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
        #driver.find_elements_by_class_name('alert alert-success-customized')
        return 1
    except Exception as ex:
        return 0


def updateSkleader(driver: WebDriver, data):
    driver.get(MAIN_URL + SKLEADER_URL)
    time.sleep(3)
    try:
        search_box_name = driver.find_element_by_name('name_contains')
        search_box_name.send_keys(data['_name'])
        time.sleep(1)
        search_box__school = driver.find_element_by_name('school_contains')
        search_box__school.send_keys(data['_school'])
        search_button = driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[2]/button')
        time.sleep(1)
        search_button.click()
        edit_skleader = driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr[1]/td[6]/a[2]/span')
        time.sleep(1)
        edit_skleader.click()

        if not pd.isna(data['_name']):
            skleader_name = driver.find_element_by_name('first_name')
            skleader_name.clear()
            time.sleep(1)
            skleader_name.send_keys(data['_name'])
        if not pd.isna(data['_email']):
            skleader_email = driver.find_element_by_name('email')
            skleader_email.clear()
            time.sleep(1)
            skleader_email.send_keys(data['_email'])
        if not pd.isna(data['_mobile']):
            skleader_mobile = driver.find_element_by_name('mobile')
            skleader_mobile.clear()
            time.sleep(1)
            skleader_mobile.send_keys(data['_mobile'])
        if not pd.isna(data['_class']):
            skleader_class = driver.find_element_by_name('student_class')
            skleader_class.clear()
            time.sleep(1)
            skleader_class.send_keys(data['_class'])
        if not pd.isna(data['_roll']):
            skleader_roll = driver.find_element_by_name('roll')
            skleader_roll.clear()
            time.sleep(1)
            skleader_roll.send_keys(data['_roll'])
        if not pd.isna(data['_gender']):
            skleader_gender = driver.find_element_by_name('gender')
            skleader_gender.send_keys(data['_gender'])
        if not pd.isna(data['_password']):
            skleader_pass = driver.find_element_by_name('password')
            skleader_pass.clear()
            time.sleep(1)
            skleader_pass.send_keys(data['_password'])
        if not pd.isna(data['_con_password']):
            skleader_con_pass = driver.find_element_by_name('confirm_password')
            skleader_con_pass.clear()
            time.sleep(1)
            skleader_con_pass.send_keys(data['_con_password'])
        time.sleep(1)

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
        update_1 = driver.find_element_by_xpath('/html/body/div/div[1]/form/section[2]/div[1]/div[1]/div/div[3]/div/div/input')
        update_1.click()
        # check that saved
        #driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
        driver.find_elements_by_class_name('alert alert-success-customized')
        return 1
    except Exception as ex:
        print(ex)
        return 0