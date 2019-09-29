import time
import pandas as pd
from selenium import webdriver
from test_ui.config import CHROME_DRIVER_LOCATION, MAIN_URL
from test_ui.test_login import login
from test_ui.test_division import addDivision
from test_ui.test_district import addDistrict
from test_ui.test_upazilla import addUpazilla
from test_ui.test_headmaster import addHeadmaster
from test_ui.test_school import addSchool
from test_ui.test_skleader import addSkleader


def main():
    driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)
    driver.get(MAIN_URL)
    time.sleep(2)
    # login
    data = pd.read_csv("test_ui/data/login.csv", dtype=str)
    for idx, row in data.iterrows():
        result = login(driver, row)
        if result == 0:
            print("Login failed")
            return
    """
    # Division data
    data = pd.read_csv("test_ui/data/division.csv", dtype=str)
    for idx, row in data.iterrows():
        addDivision(driver, row)

    # District data
    data = pd.read_csv("test_ui/data/district.csv", dtype=str)
    for idx, row in data.iterrows():
        addDistrict(driver, row)


    #Upazilla data
    data = pd.read_csv("test_ui/data/upazilla.csv", dtype=str)
    for idx, row in data.iterrows():
        addUpazilla(driver, row)

    """

     # School data
    data = pd.read_csv("test_ui/data/school.csv", dtype=str)
    for idx, row in data.iterrows():
        addSchool(driver, row)


    # Headmaster data
    data = pd.read_csv("test_ui/data/headmaster.csv", dtype=str)
    for idx, row in data.iterrows():
        addHeadmaster(driver, row)


    #Skleader data
    data = pd.read_csv("test_ui/data/skleader.csv", dtype=str)
    for idx, row in data.iterrows():
        addSkleader(driver, row)




    driver.quit()

if __name__ == "__main__":
    main()