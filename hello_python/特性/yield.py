from collections.abc import Iterator

r1 = [1, 2, 3, 4, 5]
r1.reverse()
print(r1)
print(type(r1))
print(type(r1.reverse()))
print(type(r1))

L = ['Hello', 'World', 'IBM', 'Apple']
li = [s.lower() for s in L]
print(li, type(li))
g = (s.lower() for s in L)
print(g, type(g), next(g), next(g))


def odd():
    """
    最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数
    在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
    :return:
    """
    print('step 1')
    yield 'a'
    print('step 2')
    yield ('b')
    print('step 3')
    yield ('c')


o = odd()
print(next(o), next(o))

print(isinstance(L, Iterator))
print(isinstance(iter(L), Iterator))
