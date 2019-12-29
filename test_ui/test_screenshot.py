import time
import unittest
import pandas as pd
from selenium import webdriver
from unittest import TestCase

from test_ui.test_district import addDistrict
from test_ui.test_division import addDivision
from test_ui.test_union import addUnion
from test_ui.test_upazilla import addUpazilla
from .config import *
from .test_login import login, logout
from .test_school import addSchool, deleteSchool, updateSchool
from .test_headmaster import addHeadmaster
from .test_skleader import addSkleader, updateSkleader
from .test_skmember import addSkmember

#import selenium.webdriver as webdriver
import contextlib
from selenium.webdriver.android.webdriver import WebDriver


@contextlib.contextmanager
def quitting(thing):
    yield thing
    thing.quit()


def screenShot(driver: WebDriver, data):
    quitting()
    try:

        driver.get(data['PAGE'])
        driver.implicitly_wait(2)
        driver.get_screenshot_as_file('images/'+ data['FILE_NAME']+'.png')
        return 1
    except Exception as ex:
        return 0
