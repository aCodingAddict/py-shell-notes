print('name')
True
print(True)
ss = 'abc %d . %s ded.g %.2f ht.sq' % (1, 'ss', 1.0)
fss = 'aa {0} bb {1} cc {2:.2f}'.format(1, 'ss', 1.0)
print(ss)
print(fss)
# list是一个可变的有序表,素的数据类型也可以不同
list1 = ['1', '2', 3]
print(list1)
# 可以正反索引
print(len(list1), len(list1[0]), list1[-1])
list1.append(4)
print(list1)
list1.insert(1, 5)
print(list1)
print(list1.pop(3))
print(list1)
# 元组tuple和list非常类似，但是tuple一旦初始化就不能修改.如果tuple 的元素比如是 list,那么 list 里的元素是可变的
tuple1 = ('1', '2', 3)
print(len(tuple1), tuple1[1])
print(tuple1.__contains__('1'))
int1 = (4)  # 还是 int
tuple2 = (4,)  # 成为tuple
print(int1, tuple2, type(int1), type(tuple2))

if '':
    print(True)
elif 0:
    print(True)
elif ():
    print(True)
elif []:
    print(True)
else:
    print(False)

sum1 = 0

for x in range(5):
    sum1 += x
print(sum1)
# 字典 dict,对应 map,kv存储,key必须是不可变对象,所以 list 不能作为 key
dictmap1 = {'10': 2, 11: 4}
print(dictmap1['10'])
print(dictmap1[11])
# 添加删除
dictmap1['1'] = 1
print(dictmap1)
dictmap1.pop('1')
print(dictmap1)
print(12 in dictmap1)
print(dictmap1.__contains__(11))
print(dictmap1.get('5'))  # 返回的是 None,注意：返回None的时候Python的交互环境不显示结果。

s1 = ([1, 2, 3])  # ([ ])组合相当于没有(),所以s是 list
s2 = ([1, 2, 3],)
# 要创建一个set，需要提供一个list作为输入集合
se = set([1, 2, 3])
print(type(list1), type(tuple1), type(dictmap1), type(s1), type(s2), type(se))
print(s1, s2)

# 测试
list_a = [1, 2, 3]
print(list_a)
# dict_a = {list_a: 1}  # 报错 TypeError: unhashable type: 'list'
tuple_a = (list_a, 4)
print(tuple_a)
# dict_a = {tuple_a: 1}  # 报错 TypeError: unhashable type: 'list'
tuple_b = (1, 2)
dict_b = {tuple_b: 1}  # 正常,说明,当 tuple 内部元素为可变元素时,不能作为 dict 的 key
