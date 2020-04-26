L = ['bob', 'about', 'Zoo', 'Credit']
Ls = sorted(L, key=str.lower, reverse=True)
print(Ls)


# help(max)

# help()


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1, f2, f1 == f2)
print(f1(), f2(), f1() == f2())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1, f2, f3)


def create_counter():
    def f():
        n = 0
        while True:
            n += 1
            yield n

    sum = f()

    def counter():
        return next(sum)

    return counter


print(create_counter())


def test_while():
    n = 0
    while True:
        n += 1
        yield n


o = test_while()
print(next(o), next(o))
next(o)
print(next(o))

for i in range(0, 5):
    print(i)

L = lambda x: x * x
print(L(5))
