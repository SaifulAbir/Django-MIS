from selenium import webdriver
import time
from io import BytesIO
from PIL import Image

def fullScreenShot(driver, data):
        driver = driver
        verbose = 0

        #open page
        driver.get(data['PAGE'])
        if data['FILE_NAME'] == 'School_Search':
            driver.find_element_by_id('advancedButton').click()
            time.sleep(2)
        #hide fixed header
        #js_hide_header=' var x = document.getElementsByClassName("topnavbar-wrapper ng-scope")[0];x[\'style\'] = \'display:none\';'
        #driver.execute_script(js_hide_header)

        #get total height of page
        js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'

        scrollheight = driver.execute_script(js)
        if verbose > 0:
            print(scrollheight)

        slices = []
        offset = 0
        offset_arr=[]

        #separate full screen in parts and make printscreens
        while offset < scrollheight:
            if verbose > 0:
                print(offset)

            #scroll to size of page
            if (scrollheight-offset)<offset:
                #if part of screen is the last one, we need to scroll just on rest of page
                driver.execute_script("window.scrollTo(0, %s);" % (scrollheight-offset))
                offset_arr.append(scrollheight-offset)
            else:
                driver.execute_script("window.scrollTo(0, %s);" % offset)
                offset_arr.append(offset)

            #create image (in Python 3.6 use BytesIO)
            img = Image.open(BytesIO(driver.get_screenshot_as_png()))


            offset += img.size[1]
            #append new printscreen to array
            slices.append(img)


            if verbose > 0:
                driver.get_screenshot_as_file('screen_%s.jpg' % (offset))
                print(scrollheight)

        #create image with
        screenshot = Image.new('RGB', (slices[0].size[0], scrollheight))
        offset = 0
        offset2= 0
        #now glue all images together
        for img in slices:
            screenshot.paste(img, (0, offset_arr[offset2]))
            offset += img.size[1]
            offset2+= 1

        screenshot.save('images/' + data['FILE_NAME'] + '.png')
        #driver.get_screenshot_as_file('images/' + row['FILE_NAME'] + '.png')
# fullScreenShot()