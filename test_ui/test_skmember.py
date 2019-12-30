import time

import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from .config import *

def addSkmemberEntry(driver: WebDriver, data):
    time.sleep(5)
    driver.get(MAIN_URL + SKMEMBER_URL)
    driver.find_element_by_link_text('New SK Member').click()

    time.sleep(DELAY_SHORT)
    try:
        driver.find_element_by_class_name('select2-selection__rendered').click()
        search_box = driver.find_element_by_class_name('select2-search__field')
        search_box.send_keys(data['EIIN'])
        search_box.send_keys('\n')
        skmember_name = driver.find_element_by_name('UF-first_name')
        skmember_name.send_keys(data['NAME'])
        skmember_email = driver.find_element_by_name('UF-email')
        skmember_email.send_keys(data['MOBILE'])
        skmember_mobile = driver.find_element_by_name('PF-mobile')
        skmember_mobile.send_keys(data['MOBILE'])
        skmember_class = driver.find_element_by_name('PF-student_class')
        skmember_class.send_keys(data['CLASS'])
        skmember_roll = driver.find_element_by_name('PF-roll')
        skmember_roll.send_keys('0')
        skmember_pass = driver.find_element_by_name('PF-gender')
        skmember_pass.send_keys('Male')
        time.sleep(1)
        from_date = driver.find_element_by_class_name('datepicker')
        from_date.click()
        from_date.send_keys('23-10-2010')
        time.sleep(1)
        save_button = driver.find_element_by_id('save-btn')
        save_button.click()
        # check that saved

        #driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
        driver.find_element_by_class_name('alert alert-success-customized')
        return 1
    except Exception as ex:
        return 0
    # except NoSuchElementException:
    #     return 0


def addSkmember(driver: WebDriver, data):
    driver.get(MAIN_URL + SKMEMBER_URL)
    driver.find_element_by_link_text('New SK Member').click()

    time.sleep(DELAY_SHORT)
    try:
        driver.find_element_by_class_name('select2-selection__rendered').click()
        search_box = driver.find_element_by_class_name('select2-search__field')
        search_box.send_keys(data['_eiin'])
        search_box.send_keys('\n')
        skmember_name = driver.find_element_by_name('UF-first_name')
        skmember_name.send_keys(data['_name'])
        skmember_email = driver.find_element_by_name('UF-email')
        skmember_email.send_keys(data['_email'])
        skmember_mobile = driver.find_element_by_name('PF-mobile')
        skmember_mobile.send_keys(data['_mobile'])
        skmember_class = driver.find_element_by_name('PF-student_class')
        skmember_class.send_keys(data['_class'])
        skmember_roll = driver.find_element_by_name('PF-roll')
        skmember_roll.send_keys(data['_roll'])
        skmember_pass = driver.find_element_by_name('PF-gender')
        skmember_pass.send_keys(data['_gender'])
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
    # except NoSuchElementException:
    #     return 0

def updateSkmember(driver: WebDriver, data):
    driver.get(MAIN_URL + SKMEMBER_URL)
    time.sleep(3)
    try:
        search_box_name = driver.find_element_by_name('name_contains')
        search_box_name.send_keys(data['_name'])
        time.sleep(1)
        search_box__school = driver.find_element_by_name('school_contains')
        search_box__school.send_keys(data['_school'])
        search_button = driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[2]/button')
        search_button.click()
        edit_skmember = driver.find_element_by_xpath('//*[@id="example1"]/tbody/tr[1]/td[6]/a[2]/span')
        time.sleep(1)
        edit_skmember.click()

        if not pd.isna(data['_name']):
            skmember_name = driver.find_element_by_name('first_name')
            skmember_name.clear()
            time.sleep(1)
            skmember_name.send_keys(data['_name'])
        if not pd.isna(data['_email']):
            skmember_email = driver.find_element_by_name('email')
            skmember_email.clear()
            time.sleep(1)
            skmember_email.send_keys(data['_email'])
        if not pd.isna(data['_mobile']):
            skmember_mobile = driver.find_element_by_name('mobile')
            skmember_mobile.clear()
            time.sleep(1)
            skmember_mobile.send_keys(data['_mobile'])
        if not pd.isna(data['_class']):
            skmember_class = driver.find_element_by_name('student_class')
            skmember_class.send_keys(data['_class'])
            time.sleep(1)
        if not pd.isna(data['_roll']):
            skmember_roll = driver.find_element_by_name('roll')
            skmember_roll.clear()
            time.sleep(1)
            skmember_roll.send_keys(data['_roll'])
        if not pd.isna(data['_gender']):
            skmember_gender = driver.find_element_by_name('gender')
            skmember_gender.send_keys(data['_gender'])
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
        update_1 = driver.find_element_by_xpath('/html/body/div/div[1]/form/section[2]/div[1]/div/div/div[3]/div/div/input')
        update_1.click()
        driver.find_elements_by_class_name('alert alert-success-customized')
        return 1
    except Exception as ex:
        print(ex)
        return 0

def addSkmemberOdeshboard(driver: WebDriver, data):
    driver.find_element_by_xpath('/html/body/div/aside/section/ul[2]/li[3]/a/span').click()
    time.sleep(1)
    driver.find_element_by_link_text('New SK Member').click()

    time.sleep(DELAY_SHORT)
    try:
        skmember_name = driver.find_element_by_name('UF-first_name')
        skmember_name.send_keys(data['_name'])
        skmember_email = driver.find_element_by_name('UF-email')
        skmember_email.send_keys(data['_email'])
        skmember_mobile = driver.find_element_by_name('PF-mobile')
        skmember_mobile.send_keys(data['_mobile'])
        skmember_class = driver.find_element_by_name('PF-student_class')
        skmember_class.send_keys(data['_class'])
        skmember_roll = driver.find_element_by_name('PF-roll')
        skmember_roll.send_keys(data['_roll'])
        skmember_pass = driver.find_element_by_name('PF-gender')
        skmember_pass.send_keys(data['_gender'])
        time.sleep(1)
        # from_date = driver.find_element_by_class_name('datepicker')
        # from_date.click()
        # from_date.send_keys(data['DATE'])
        save_button = driver.find_element_by_id('save-btn')
        save_button.click()
        # check that saved

        driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
        # driver.find_elements_by_class_name('alert alert-success-customized')
        return 1
    except Exception as ex:
        return 0
    # except NoSuchElementException:
    #     return 0