#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = dir(TimeoutError)

print(a)

b = hasattr(TimeoutError, "__init__")
c = getattr(TimeoutError, "__init__")
d = getattr(TimeoutError, "A", 404)

print(d)


class Test1:
    pass


t = Test1()

print(t)
