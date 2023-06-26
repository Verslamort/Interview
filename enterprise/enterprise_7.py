# 求出列表所有奇数并构造新列表
# 方法1 列表推导式
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [i for i in a if i % 2 == 1]
print(b)


# 方法2 使用filter
def fn(a):
    return a % 2 == 1


c = filter(fn, a)
c = [i for i in c]
print(c)
