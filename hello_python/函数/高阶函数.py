#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
高阶函数
    1. 变量可以指向函数
    2. 函数名也是变量
    3. 函数可以作为参数传入另一个函数
    4. 函数可以作为返回值
"""

__author__ = 'XueKai_aCodingAddict'


s = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(s))

s = '1122'
s.upper()
print(s)


def normalize(name):
    if isinstance(name, str):
        n1 = name.lower()
    else:
        return
    name = n1[0].upper() + n1[1:]
    return name


print(normalize("batT"))

t = "aaAA"
t1 = t.upper()
print(t1)


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())  # 9,9,9
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 匿名函数 lambda x : ?
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
f = lambda x: x * x
print(f(5))

# 装饰器(Decorator):不修改函数的同时增强函数的功能,在代码运行期间动态增加功能的方式.本质上，decorator就是一个返回函数的高阶函数.
# 取函数名
d = count
print(f.__name__, d.__name__)


def decor(fu):
    def tmp():
        print("aaa")
        return fu()
    return tmp


import datetime


@decor  # 相当于 time = decor(time)
def time():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


time()
print(time.__name__)  # tmp

import functools


def decor(fu):
    # 在定义tmp()的前面把原始fu()函数的__name__等属性复制到tmp()函数中
    @functools.wraps(fu)
    def tmp():
        print("aaa")
        return fu()
    return tmp


@decor  # 相当于 time = decor(time)
def time():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


time()
print(time.__name__)  # time


# 偏函数（Partial function）,和数学意义上的偏函数不一样。
# functools.partial就是用来创建一个偏函数
# 把一个函数的某些参数给固定住（也就是设置默认值）,返回一个新的函数,但也可以在函数调用时传入其他值,可以接收函数对象、*args和**kw这3个参数
a = int("1234")
print(a, type(a))
# 进制转换
b = int("11111", base=2)
print(b, type(b))
int2 = functools.partial(int, base=2)
c = int2("11111")
print(c, type(c))
d = int2("11111", base=8)
print(d)

a = max(1, 2, 3)
print(a)
max2 = functools.partial(max, 4)  # 相当于max(*args, 4)
b = max2(1, 2, 3)
print(b)


def c(*args):
    return args


d = c()
print(d)
