#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/9/8 16:27
import os
from appium import webdriver
from PIL import Image
import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

logging.basicConfig(level=logging.INFO)

desired_caps = {
  "platformName": "Android",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.zhihu.android",
  "appActivity": ".app.ui.activity.MainActivity"
}
server = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(server, desired_caps)

sleep(4)
el1 = driver.find_element_by_id("com.zhihu.android:id/captcha_image_input_view")
el1.click()
# TouchAction(driver).press(x=491, y=485).move_to(x=630, y=550).release().perform()
sleep(5)
el3 = driver.find_element_by_id("com.zhihu.android:id/view_guide_info")
el3.click()
# el4 = driver.find_element_by_id("com.zhihu.android:id/login_username")
# el4.click()
# el4.send_keys("13")
# el5 = driver.find_element_by_id("com.zhihu.android:id/login_password")
# el5.send_keys("1321")
# el6 = driver.find_element_by_id("com.zhihu.android:id/captcha_image_input_view")
# el6.send_keys("1321")


def identifyingCode(driver, startx, starty, endx, endy):
    u'''获取验证码
    （startx，xstarty）---------------------------------
                      |     要截取的图片范围           |
                      |                                |
                      ---------------------------------- (endx,endy)
    '''
    driver.get_screenshot_as_file(os.getcwd() + '\\cirsschan.png')
    imGetScreen = Image.open(os.getcwd() + '\\cirsschan.png')
    box = (startx, starty, endx, endy)
    imIndentigy = imGetScreen.crop(box)
    imIndentigy.save(os.getcwd() + '\\indent.png')
    strCommand = 'tesseract.exe ' + os.getcwd() + '\\indent.png ' + os.getcwd() + '\\indet'
    print(strCommand)
    os.system(strCommand)
    rfindet = open(os.getcwd() + '\\indet.txt', 'r')
    strIndet = rfindet.readline().encode('utf-8')
    print(strIndet)
    return strIndet


identifyingCode(driver, 476, 479, 642, 558)
driver.quit()