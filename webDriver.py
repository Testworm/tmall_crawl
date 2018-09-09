#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Torre Yang
# datetime:2018/9/9 19:58
from selenium import webdriver
import os
from time import sleep


def chromeDriver(url):
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url)
    return driver


def firefoxDriver(url):
    option = webdriver.FirefoxOptions()
    option.add_argument("headless")
    driver = webdriver.Firefox(firefox_options=option)
    driver.get(url)
    return driver