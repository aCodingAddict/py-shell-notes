#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-08-29 13:11 八月
# @Author  : XueKai_aCodingAddict

"""
多重继承、定制类、元类等概念
"""


class Student(object):
    pass


# 给实例动态绑定属性
s = Student()
s.name = 'a'
print(s.name)


# 给实例动态绑定方法
# 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age


from types import MethodType

# 给实例绑定一个方法,只对这个实例有作用,不会影响其他实例
s.set_age = MethodType(set_age, s)
s.set_age(5)
print(s.age)
s1 = Student()
# print(s1.age)  # AttributeError: 'Student' object has no attribute 'age'
# s1.set_age(6)  # AttributeError: 'Student' object has no attribute 'set_age'

# 给类绑定一个方法,对所有实例起作用
Student.set_age = set_age
s1.set_age(6)
print(s1.age)

'''
使用__slots__来限制该类的实例能添加的属性
'''


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s2 = Student()
# s2.score = 30  # AttributeError: 'Student' object has no attribute 'score'
Student.__slots__ = ('name', 'age', 'score')
# s2.score = 30  # 只能在定义类时添加

# __slots__定义的属性仅对当前类的实例起作用，对继承的子类是不起作用的


class SubStudent(Student):
    pass


s3 = SubStudent()
s3.name = 'a'
s3.parent = 'ab'
print(s3.name, s3.parent)

# 在子类中也定义__slots__，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


class SubStudent(Student):
    __slots__ = ('score',)


s4 = SubStudent()
s4.name = 'b'
s4.score = 30
# s4.parent = 'ab'  # AttributeError: 'SubStudent' object has no attribute 'parent'
