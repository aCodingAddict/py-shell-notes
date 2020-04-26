import math

help(abs)
help(max)


def udf(n):
    if n > 1:
        pass
    elif n < 1:
        return n
    else:
        return None


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(100, 100, 60, math.pi / 6))
x, y = move(100, 100, 60, math.pi / 6)
print(x)
print(y)

print(isinstance(x, (int, float, bool)))
