#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-08-26 19:11 八月
# @Author  : XueKai_aCodingAddict

"""
doc
"""

import functools
import sys

max2 = functools.partial(max, 10)
print(max2(1, 2, 3))  # max(10,1,2,3)

args = sys.argv  # list存储命令行参数,至少有一个元素，因为第一个参数永远是该.py文件的名称
print(args)

# 直接运行此模块时,Python解释器把一个特殊变量__name__置为__main__,而在其他地方导入此模块时_name_ != _main_
print(__name__)
print(__doc__)


class Student1(object):
    pass


s1 = Student1()
print(s1)


class Student2(object):
    # self表示实例本身
    def __init__(self, name, age, grade):
        self.name = name
        self._age = age
        self.__grade = grade

    def get_grade(self):
        return self.__grade


s2 = Student2("a", 1, 5)
print(s2)
print(s2.name)
print(s2._age)
# print(s2._grade)  # AttributeError: 'Student2' object has no attribute '_grade'
print(s2._Student2__grade)
print("================================")
print(s2.get_grade())
# 这里其实是给实例s2设置了一个新的变量__grade,因为python解释器已经把s2内部的__grade转换了变量名,比如_Student2__grade
s2.__grade = 9
print(s2.__grade)
print(s2.get_grade())
s2._Student2__grade = 10
print(s2.get_grade())
print(s2._Student2__grade)