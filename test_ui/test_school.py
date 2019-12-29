import time
from datetime import date

import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from .config import *


def addSchool(driver: WebDriver, data):
    driver.get(MAIN_URL + SCHOOL_URL)
    add_school = driver.find_element_by_link_text('New School')
    add_school.click()
    time.sleep(2)
    try:
        new_sc_name = driver.find_element_by_name('name')
        new_sc_name.send_keys(data['_school_name'])

        if not pd.isna(data['_eiin']):
            school_id = driver.find_element_by_name('school_id')
            school_id.send_keys(data['_eiin'])

        if not pd.isna(data['_eiin']):
            club_establishment_date = driver.find_element_by_name('club_establishment_date')
            club_establishment_date.send_keys('24-12-2019')

        if not pd.isna(data['_upazila']):
            school_address = driver.find_element_by_name('address')
            school_address.send_keys(data['_upazila'])
        time.sleep(1)
        if not pd.isna(data['_division']):
            division_name = Select(driver.find_element_by_name('division'))
            division_name.select_by_visible_text(data['_division'])
        time.sleep(1)
        if not pd.isna(data['_district']):
            district_name = Select(driver.find_element_by_name('district'))
            district_name.select_by_visible_text(data['_district'])
        time.sleep(1)
        if not pd.isna(data['_upazila']):
            upazilla_name = Select(driver.find_element_by_name('upazilla'))
            upazilla_name.select_by_visible_text(data['_upazila'])
        time.sleep(1)
        if not pd.isna(data['_union']):
            union_name = Select(driver.find_element_by_name('union'))
            union_name.select_by_visible_text(data['_union'])
            time.sleep(1)
        save_button = driver.find_element_by_id('save-btn')
        save_button.click()
        time.sleep(2)
        driver.find_element_by_css_selector('div[class="alert alert-success-customized"')
        return 1
    except Exception as ex:
        return 0


def deleteSchool(driver: WebDriver, data):
    driver.get(MAIN_URL + SCHOOL_URL)
    try:
        search_box = driver.find_element_by_xpath('//*[@id="example1_filter"]/label/input')
        search_box.send_keys(data['_eiin'])
        time.sleep(1)
        trash_button = driver.find_element_by_class_name('js-delete-school')
        trash_button.click()
        time.sleep(1)
        delete_button = driver.find_element_by_xpath("//*[contains(text(), 'Delete')]")
        delete_button.click()
        time.sleep(1)
        driver.find_element_by_id('alertdiv')
        return 1
    except Exception as ex:
         return 0


def updateSchool(driver: WebDriver, data):
    driver.get(MAIN_URL + SCHOOL_URL)
    try:
        name_search_box = driver.find_element_by_name('name_contains')
        name_search_box.send_keys(data['_school_name'])
        time.sleep(1)
        schoolID_search_box = driver.find_element_by_name('school_id_contains')
        schoolID_search_box.send_keys(data['_eiin_old'])
        time.sleep(1)
        # division_search_box = driver.find_element_by_name('division_contains')
        # division_search_box.send_keys(data['_division'])
        # time.sleep(1)
        # district_search_box = driver.find_element_by_name('district_contains')
        # district_search_box.send_keys(data['_district'])
        # time.sleep(1)
        # upazila_search_box = driver.find_element_by_name('upazilla_contains')
        # upazila_search_box.send_keys(data['_upazila'])
        # time.sleep(1)
        # union_search_box = driver.find_element_by_name('union_contains')
        # union_search_box.send_keys(data['_union'])
        # time.sleep(1)

        search_school = driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div[1]/div/form/div[3]/button[1]')
        search_school.click()
        time.sleep(1)

        # view_school = driver.find_element_by_xpath('//*[@id="ab"]/a[1]/span')
        # view_school.click()
        update_school = driver.find_element_by_xpath('//*[@id="ab"]/a[2]/span')
        update_school.click()


        # update_school = driver.find_element_by_xpath('//*[@id="ab"]/a[2]/span')
        # update_school.click()
        time.sleep(2)

        if not pd.isna(data['_school_name']):
            new_sc_name = driver.find_element_by_name('name')
            new_sc_name.clear()
            new_sc_name.send_keys(data['_school_name'])

        if not pd.isna(data['_eiin_new']):
            school_id = driver.find_element_by_name('school_id')
            school_id.clear()
            school_id.send_keys(data['_eiin_new'])

        if not pd.isna(data['_upazila']):
            school_address = driver.find_element_by_name('address')
            school_address.clear()
            school_address.send_keys(data['_upazila'])
        time.sleep(2)
        if not pd.isna(data['_division']):
            division_name = Select(driver.find_element_by_name('division'))
            division_name.select_by_visible_text('---------')
            division_name.select_by_visible_text(data['_division'])

        time.sleep(2)
        if not pd.isna(data['_district']):
            district_name = Select(driver.find_element_by_name('district'))
            district_name.select_by_visible_text('---------')
            district_name.select_by_visible_text(data['_district'])
        time.sleep(2)
        if not pd.isna(data['_upazila']):
            upazilla_name = Select(driver.find_element_by_name('upazilla'))
            upazilla_name.select_by_visible_text('---------')
            upazilla_name.select_by_visible_text(data['_upazila'])
        time.sleep(1)
        if not pd.isna(data['_union']):
            union_name = Select(driver.find_element_by_name('union'))
            union_name.select_by_visible_text('---------')
            union_name.select_by_visible_text(data['_union'])
        save_button = driver.find_element_by_id('save-btn')
        save_button.click()
        time.sleep(1)
        driver.find_elements_by_class_name('alert alert-success-customized')
        return 1
    except Exception as ex:
        return 0


