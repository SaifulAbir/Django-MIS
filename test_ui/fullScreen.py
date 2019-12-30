import driver as driver
from selenium import webdriver
import selenium.webdriver as webdriver
import time
from io import BytesIO
from PIL import Image
from selenium.webdriver.chrome.webdriver import WebDriver


def fullScreenShot(driver: WebDriver, data):
        verbose = 0
        driver.get(data['PAGE'])
        if data['FILE_NAME'] == 'School_Search':
            driver.find_element_by_id('advancedButton').click()
            time.sleep(2)

        if data['FILE_NAME'] == 'Event_Week':
            driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[2]').click()
            time.sleep(1)
        elif data['FILE_NAME'] == 'Event_Day':
            driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[3]').click()
            time.sleep(1)
        elif data['FILE_NAME'] == 'Event_Event_List':
            driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[4]').click()
            time.sleep(1)
        elif data['FILE_NAME'] == 'Division_add':
            driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div/div[1]/button').click()
            time.sleep(1)
        elif data['FILE_NAME'] == 'District_add':
            driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div[1]/button').click()
            time.sleep(1)
        elif data['FILE_NAME'] == 'Upazila_add':
            driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div[1]/button').click()
            time.sleep(1)
        elif data['FILE_NAME'] == 'Union_add':
            driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div[1]/button').click()
            time.sleep(1)
        elif data['FILE_NAME'] == 'Topic_add':
            driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div/div/div[1]/button').click()
            time.sleep(1)

        js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'

        scrollheight = driver.execute_script(js)
        if verbose > 0:
            print(scrollheight)

        slices = []
        offset = 0
        offset_arr=[]

        while offset < scrollheight:
            if verbose > 0:
                print(offset)

            if (scrollheight-offset)<offset:
                driver.execute_script("window.scrollTo(0, %s);" % (scrollheight-offset))
                offset_arr.append(scrollheight-offset)
            else:
                driver.execute_script("window.scrollTo(0, %s);" % offset)
                offset_arr.append(offset)

            img = Image.open(BytesIO(driver.get_screenshot_as_png()))

            offset += img.size[1]
            slices.append(img)


            if verbose > 0:
                driver.get_screenshot_as_file('screen_%s.jpg' % (offset))
                print(scrollheight)

        screenshot = Image.new('RGB', (slices[0].size[0], scrollheight))
        offset = 0
        offset2= 0

        for img in slices:
            screenshot.paste(img, (0, offset_arr[offset2]))
            offset += img.size[1]
            offset2+= 1

        screenshot.save('images/' + data['FILE_NAME'] + '.png')
