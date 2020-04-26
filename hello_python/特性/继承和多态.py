#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DOCUMENT
"""
__author__ = 'XueKai_aCodingAddict'

import types


class Animal(object):
    def run(self):
        print("animal run")


class Dog(Animal):
    def run(self):
        print("dog run")


d = Dog()
d.run()


def fn():
    pass


print(
    type(fn) == types.FunctionType,
    type(abs) == types.BuiltinFunctionType,
    type(lambda x: x) == types.LambdaType,
    type((x for x in range(10))) == types.GeneratorType,
    isinstance(fn, types.FunctionType),
    type(fn),
    types.FunctionType
)
