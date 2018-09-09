#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/9/6 9:32
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(dict(zip(a, b)))

import os
import subprocess

cmd = 'tesseract.exe D:\PycharmProjects\\tmall_crawl_reviews\indent.png D:\PycharmProjects\\tmall_crawl_reviews\indet'
print(cmd)
if os.system(cmd):
    print('执行失败')
else:
    print('成功')

# print(os.system(cmd))
subprocess.getstatusoutput('tesseract.exe D:\PycharmProjects\tmall_crawl_reviews\indent.png D:\PycharmProjects\tmall_crawl_reviews\indet')