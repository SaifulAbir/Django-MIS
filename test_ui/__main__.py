import time

from selenium import webdriver
from test_ui.config import CHROME_DRIVER_LOCATION, MAIN_URL
from test_ui.test_login import login
from test_ui.test_school import addSchool


def main():
    driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)
    driver.get(MAIN_URL)
    time.sleep(2)
    login(driver)
    time.sleep(2)
    addSchool(driver)
    driver.quit()

if __name__ == "__main__":
    main()