# 用一行python代码写出1+2+3+10248
from functools import reduce


# 方法1 使用sum
a = [1, 2, 3, 10248]
b = sum(a)
print(b)


# 方法2
def add(x, y):
    return x + y


s1 = reduce(add, a)
print(s1)


# 法3
s2 = reduce(lambda x, y: x + y, a)
print(s2)
