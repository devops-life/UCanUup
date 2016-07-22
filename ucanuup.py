#!/usr/bin/env python
# encoding: utf-8

# 新式类
__metaclass__ = type

"""
@author: chenzhangpeng
@contact: chen_zhangpeng@163.com
@file: ucanuup.py
@time: 16/7/22 上午10:25
"""

import urllib2
import re
"""
    获取UCloud.txt内容
"""
res = urllib2.urlopen('http://106.75.28.160/UCloud.txt')
html = res.read()

# print html.count('UCanUup')

pattern = re.compile('UCanUup')

match = pattern.findall(html)

if match:
    print len(match)