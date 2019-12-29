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
from .test_login import login, logout, updateProfile
from .test_school import addSchool, deleteSchool, updateSchool
from .test_headmaster import addHeadmaster, updateHeadmaster
from .test_skleader import addSkleader, updateSkleader
from .test_skmember import addSkmember, updateSkmember, addSkmemberOdeshboard


class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)
        self.driver.get(MAIN_URL)
        time.sleep(DELAY_SHORT)

    def testLogin(self):
        data = pd.read_csv("test_ui/testdata/login.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = login(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
            if actual == 1: logout(self.driver)
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testSchool(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'Admin'})
        data = pd.read_csv("test_ui/testdata/school_entry.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = addSchool(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print( row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testHeadmaster(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/headmaster_entry.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = addHeadmaster(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testSkleader(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/skleader_entry.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = addSkleader(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testSkmember(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/skmember_entry.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = addSkmember(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testDivision(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/division_entry.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = addDivision(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testDistrict(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/district_entry.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = addDistrict(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testUpazilla(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/upazilla_entry.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = addUpazilla(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testUnion(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/union_entry.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = addUnion(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testDeleteSchool(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/schoolDelete.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = deleteSchool(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testUpdateSchool(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/school_update.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = updateSchool(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testUpdateHeadmaster(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/headmaster_update.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = updateHeadmaster(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testUpdateSkleader(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/skleader_update.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = updateSkleader(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testUpdateSkmember(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/skmember_update.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = updateSkmember(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testSkmemberOtherDashboard(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/skmember_update.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = addSkmemberOdeshboard(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")

    def testUpdateProfile(self):
        login(self.driver, {'_email': 'admin', '_password': 'sk071219', 'name': 'admin'})
        data = pd.read_csv("test_ui/testdata/profile_update.csv", dtype=str)
        f = 0
        for idx, row in data.iterrows():
            actual = updateProfile(self.driver, row)
            try:
                self.assertEqual(row['expected_result'], str(actual))
                print(
                    row['test_case_id'] + " Expected " + row['expected_result'] + " Pass : " + row['test_description'])
            except Exception as ex:
                print(row['test_case_id'] + " Expected " + row['expected_result'] + " Failed : " + row['test_description'])
                print(ex)
                f = f + 1
        if f != 0:
            raise Exception("Total pass: " + str(idx + 1 - f) + " and Failed: " + str(f))
        else:
            print("All passed")


if __name__ == '__main__':
    unittest.main()
