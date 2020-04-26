#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-08-26 19:11 八月
# @Author  : XueKai_aCodingAddict

"""
DOCUMENT
"""


class Test1(object):
    def __init__(self, a):
        pass


# 使用type()显示类型
b = Test1(1)
print(type(b))
print(type(1) == int)
print(type("abc") == str)


class Test2(Test1):
    def __init__(self, c):
        pass


# 使用isinstance()判断继承关系
d = Test2(2)
print(isinstance(d, Test1))
print(isinstance(d, (Test1, Test2)))

# 使用types模块常量判断函数类型
import types

print(types.FunctionType)
print(type(Test1.__init__))

# dir()获取一个对象的所有属性和方法,返回包含字符串的list
print(dir(d))

# 使用len()获取对象长度,其实内部调用的是对象的特殊函数__len__()方法,len(s)=s.__len__()
s = "123"
print(dir(s))
print(len(s))

# hasattr(obj, 'x')是否有属性或方法x
print(hasattr(s, "x"))
print(hasattr(s, "__len__"))

# setattr(obj, 'y', 19)给已有的属性设置值
# setattr(s, 'x', 123)  # AttributeError: 'str' object has no attribute 'x'
print(hasattr(s, '__len__'), getattr(s, '__len__'), s.__len__)
# 没有这个属性就返回默认值
print(getattr(s, 'x', 404))


# print(setattr(s, 'x', 101))  # AttributeError: 'str' object has no attribute 'x'


class TestClass(object):
    # 类属性,归类所有,但是所有的实例都可以访问
    name = 'test'

    # 实例属性通过self绑定
    def __init__(self, age):
        self.age = age
        pass


a = TestClass(20)
print(a.name)  # test
print(TestClass.name)  # test
a.name = 'class'
print(a.name)  # class,所以实例属性值的改变不会影响类属性的值.实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(TestClass.name)  # test
