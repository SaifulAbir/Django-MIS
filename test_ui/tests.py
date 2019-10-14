import time
import unittest
import pandas as pd
from selenium import webdriver

from test_ui.config import CHROME_DRIVER_LOCATION, MAIN_URL
from test_ui.test_login import login, logout
from test_ui.test_school import addSchool


class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)
        self.driver.get(MAIN_URL)
        time.sleep(2)

    def testLogin(self):
        data = pd.read_csv("test_ui/testdata/login.csv", dtype=str)
        for idx, row in data.iterrows():
            actual = login(self.driver, row)
            self.assertEqual( row['expected'], str(actual))
            if actual == 1: logout(self.driver)

    def testSchool(self):
        login(self.driver, {'email':'admin', 'password': '123', 'name': 'Admin'})
        data = pd.read_csv("test_ui/testdata/school.csv", dtype=str)
        for idx, row in data.iterrows():
            actual = addSchool(self.driver, row)
            self.assertEqual( row['expected'], str(actual))

if __name__ == '__main__':
    unittest.main()