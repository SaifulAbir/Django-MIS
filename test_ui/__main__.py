import time
import pandas as pd
from selenium import webdriver
from test_ui.config import CHROME_DRIVER_LOCATION, MAIN_URL
from test_ui.test_login import login
from test_ui.test_school import addSchool


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

    # School data
    data = pd.read_csv("test_ui/data/school.csv", dtype=str)
    for idx, row in data.iterrows():
        addSchool(driver, row)


    driver.quit()

if __name__ == "__main__":
    main()