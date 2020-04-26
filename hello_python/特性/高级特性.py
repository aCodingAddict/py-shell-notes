from collections.abc import Iterator
from collections.abc import Iterable

r = []
print(r)
# r.append()
# r.insert()
# r.pop()
# r.clear()
# r.copy()
# r.count()
# r.index()
# r.reverse()
# r.sort()
# r.extend()
# r.remove()
r1 = [1]
r2 = r.__add__(r1).__add__(r1)
print(r2, type(r2))
# 切片
print(r2[0:2], r2[-2:-1], r2[-1])

s = ' 123 '
print(len(s))
print(range(5))
for n in range(4, 5):
    print(n)
print("=============================")
print(isinstance(s, (Iterable,)))
print(isinstance(s, str))
# 迭代
for i in s:
    print(i)
# enumerate函数可以把一个list变成 索引-元素 对
k = enumerate(s)
print(k)  # <enumerate object at 0x1065b9780>
for i, j in k:
    print(i, j)

print(len(r))

r3 = [1, 2, 3, 4, 5]
r4 = ["1", "2", "3", "4"]
print(max(*enumerate(r4)))

# 列表生成式
r5 = list(range(0, 5))
print(r5)

print("================================================")
r3.reverse()
print(r3)
print(r4)

a = [x * y for x in r3 for y in r4]
print(isinstance(a, list))  # true

print([x * y for x in r3 if x % 2 == 0 for y in r4])
n1 = "1"
n2 = 0
print([n1 * n2])

# 双循环
[m + n for m in 'ABC' for n in 'XYZ']  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 如果把列表生成式的[]变为(),就变成了一个生成器 generator,可以一边循环一边计算,不会浪费空间
g = (x * x for x in range(10))
print(g, type(g))
# 通过 next(g)获取,每次调用就计算出下一个值,也可以用 for in 循环
a = next(g)
print(a)
print("===================")

# for循环的数据类型有以下几种：统称为可迭代对象：Iterable
#
# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是 generator，包括生成器和带yield的generator function。
#
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# generator 是 Iterator,但是 list 等不是.使用 iter() 可以把 list 等对象转换为迭代器

print(isinstance(r2, Iterator))
print(isinstance(iter(r2), Iterator))


# 斐波那契数列（Fibonacci）: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


a = fib(10)
print(a)


# 用关键字 yield 改造成生成器函数 generator function
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


a = fib(10)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
# next(a)  # StopIteration: done

print("=====================")
b = fib(10)
while True:
    try:
        c = next(b)
    except StopIteration:
        break


