s1 = 'C'
s2 = ' '
s3 = ' AB C'
print(s2.strip())
print(s2 and s2.strip())
print(s3 and s3.strip())
print("======================")


def not_empty(s):
    b = s and s.strip()
    print(s, b)
    return b


l1 = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(l1)

print("======================")


def is_odd(n):
    b = n % 2 == 1
    print(n, b)
    return b


l2 = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(l2)

print("======================")
l3 = [1, "2", 3.0, "", "   ", " A ", None]  # "",None为false,其余为true
l4 = set(filter(None, l3))
print(l4)

s4 = '12321'
print(s4[3] == s4[-3], s4[3], s4[-3])

i1 = 12321
s5 = str(i1)
print(s5, type(s5))


def is_palindrome(n):
    n = str(n)
    indices = range(len(n))
    for index in indices:
        if index >= len(n) // 2:
            return True
        if n[index] != n[-index - 1]:
            return False


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print(is_palindrome(1))
