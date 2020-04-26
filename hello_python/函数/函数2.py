# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数


# 默认参数,=
def default_params(x, y=1, z="n"):
    print(x, y, z)


default_params(1, 2, 3)
default_params(11)
default_params(111, z='nnn')


# 可变参数
def variable_params(*x):
    print(x, type(x))


variable_params(12, "111", [1, "2"])
variable_params()
list1 = [1, 2, "n"]
default_params(*list1)
list1 = [1, 2, "m"]
default_params(list1)
print(type(list1))
variable_params(*list1)  # (1, 2, 'm') <class 'tuple'>
variable_params(list1)  # ([1, 2, 'm'],) <class 'tuple'>


# 关键字参数,key=value
def person(name, age, **x):
    print(name, age, x, type(x))


person("a", 10)  # a 10 {}  <class 'dict'>
person("a", 18, city="北京", address='立水桥')
dict1 = {'city': "北京", 'adress': '立水桥'}
person('b', 20, **dict1)
person('b', 20, **dict1, test=1)
person('b', 20, city='bj', address='lsq', test=1)


# 命名关键字参数,*分割后的k=v,可变参数+命名关键字不需要*分割 -> def person1(name, age, *args, city):
def person1(name, age, *, city):
    print(name, age, city)


person1("c", 22, city="bj")
# TypeError: person1() missing 1 required keyword-only argument: 'city'
# person1("d", 24)
# person1("d", 24, )
# TypeError: person1() got an unexpected keyword argument 'address'
# person1("d", 24, address='')

s = dict1.get("city")
print(s)


# 测试
def test1(*a):
    print("2")


def test1():
    print("1")


test1()  # 后一个会把前一个覆盖
# test1(1)  # 报错 TypeError: test1() takes 0 positional arguments but 1 was given
