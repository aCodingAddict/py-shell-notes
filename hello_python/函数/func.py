#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DOCUMENT
"""

__author__ = 'XueKai_aCodingAddict'

from functools import reduce

import sys

print(__doc__)
print(__name__)
print(__author__)
print(sys.path)

li = [1, 2, -3, 4]


def func1():
    pass


def func2(a, b):
    pass


def func3(a):
    pass


map(func1, li)  # 对li的每个元素进行func1(一个参数),li必须是Iterable,返回的是Iterator
reduce(func2, li)  # 对每个元素和下一个元素就行func2(两个参数)
filter(func3, li)  # 对每个元素根据func3进行过滤
len(li)  # 长度
list(li)  # 生成list
tuple(li)  # 生成tuple
set(li)  # 生成set
isinstance(li, list)  # 类型匹配
max(li)  # 求最大值
min(li)  # 求最小值
sum(li)  # 求和
range(1, 5)  # 生成range
reversed(li)  # 生成新的反转的
enumerate(li)  # 将下标与值一一对应
sorted(li, key=abs, reverse=True)  # 默认升序排序,reverse反向,abs取绝对值
abs(-1)  # 绝对值

print(abs(-1))

help(func2)  # func1信息
