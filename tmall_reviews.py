#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/9/3 16:52

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import webDriver
import csv
import logging
logging.basicConfig(level=logging.INFO)
import htmlRes


# 读取商品列表 <全球购一号店>; 商品信息csv文件
def productReader(file):
    with open(file, 'r', encoding='gbk') as f:
        tar = csv.reader(f)
        products = []
        for row in tar:
            products.append(row[1].strip())
        logging.info("读取商品列表完毕")
    return products


# 获取网站信息, 1.获取网易考拉; 2.获取天猫


# 获取评论列表存至list, 保存格式为:


# 商品比价部分, 输出价格最高TOP5; 1.获取网易考拉; 2.获取天猫; 商品+价格+链接
def getPrice(product, type):
    if type == 1:
        baseUrl = 'https://www.kaola.com/'
        soup = htmlRes.getKaolaHtml(product)

    else:
        TmallUrl = 'https://list.tmall.com/search_product.htm?q='+product+'&sort=d'
        driver = webDriver.chromeDriver(url=TmallUrl)
        prices = driver.find_elements_by_css_selector('p.productPrice em')
        pUrls = driver.find_elements_by_css_selector('p.productTitle a')
        # 输出销量前2名
        pt = zip(prices, pUrls)
        for price, pUrl in pt:
            # print(price.get_attribute('title'))
            print(pUrl.get_attribute('title'), price.get_attribute('title'), pUrl.get_attribute('href'))









if __name__=='__main__':
    products = productReader('Global.csv')
    for product in products:
        getPrice(product, 2)


