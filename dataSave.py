#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/9/7 18:46
import pymongo

# 关系型数据库
# 保存为插入SQL语句
data = {
    'id': '2001',
    'name': 'Torre',
    'age': '20'
}
table = 'student'
keys = ','.join(data.keys())
# values = ','.join(data.values())
values = ','.join(['%s']*len(data))
print(keys)
print(values)
print(tuple(data.values()))
sql = 'Insert into {table} ({keys}) values ({values})'.format(table=table, keys=keys, values=values)
print(sql)
print(sql, tuple(data.values()))

try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successfull')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()

# 非关系型数据库  NOT ONLY SQL




