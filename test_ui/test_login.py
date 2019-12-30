import os
import time

from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from .config import *
from selenium.webdriver.ie.webdriver import WebDriver


def login(driver, data):
    try:
        driver.find_elements_by_xpath("//*[contains(text(), 'Sign In')]")
        admin_name = driver.find_element_by_name('email')
        admin_name.clear()
        admin_name.send_keys(data['_email'])
        admin_pass = driver.find_element_by_name('password')
        admin_pass.send_keys(data['_password'])
        admin_pass.submit()
        time.sleep(DELAY_SHORT)
        try:
            driver.find_element_by_class_name('dropdown-toggle')
            return 1
        except NoSuchElementException:
            return 0
    except NoSuchElementException:
        return 1

    # if data['email'] == data['name']:
    #     admin_pass.submit()
    #     time.sleep(DELAY_LONG)
    #     try:
    #         driver.find_element_by_link_text(data['name'])
    #         return 1
    #     except NoSuchElementException:
    #         return 0
    # else:
    #     return 0


def logout(driver):
    profile_name = driver.find_element_by_class_name('dropdown-toggle')
    profile_name.click()
    time.sleep(DELAY_SHORT)
    sign_out = driver.find_element_by_link_text('Sign out')
    sign_out.click()
    time.sleep(DELAY_SHORT)


def updateProfile(driver: WebDriver, data):
    profile_name = driver.find_element_by_class_name('dropdown-toggle')
    profile_name.click()
    driver.find_element_by_link_text('Profile').click()
    time.sleep(DELAY_SHORT)
    driver.find_element_by_link_text('Edit Profile').click()
    time.sleep(DELAY_SHORT)
    try:
        if not pd.isna(data['_name']):
            try:
                profile_name = driver.find_element_by_name('PF-first_name')
            except:
                profile_name = driver.find_element_by_name('first_name')
            profile_name.clear()
            profile_name.send_keys(data['_name'])
            time.sleep(1)
        if not pd.isna(data['_email']):
            try:
                profile_email = driver.find_element_by_name('PF-email')
            except:
                profile_email = driver.find_element_by_name('email')
            profile_email.clear()
            profile_email.send_keys(data['_email'])
            time.sleep(1)
        if not pd.isna(data['_password']):
            try:
                profile_password = driver.find_element_by_name('PF-password')
            except:
                profile_password = driver.find_element_by_name('password')
            profile_password.clear()
            profile_password.send_keys(data['_password'])
            time.sleep(1)
        if not pd.isna(data['_con_password']):
            try:
                profile_con_password = driver.find_element_by_name('PF-confirm_password')
            except:
                profile_con_password = driver.find_element_by_name('confirm_password')
            profile_con_password.clear()
            profile_con_password.send_keys(data['_con_password'])
            time.sleep(1)
        #
        # profile_image = driver.find_element_by_id('id_PF-image').click()
        # time.sleep(1)
        # profile_image.send_keys("/images/profile.jpg")
        # time.sleep(1)

        save_button = driver.find_element_by_id('save-btn')
        save_button.click()
        time.sleep(DELAY_LONG)
        driver.find_element_by_link_text('Edit Profile')
        return 1
    except Exception as ex:
        return 0
