# Python-遍历列表时删除元素的正确做法
# 方法1 分两张表
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = a[:]
for i in a:
    if i > 5:
        pass
    else:
        b.remove(i)
print(b)


# 方法2 使用filter
c = filter(lambda x: x > 5, a)
print(list(c))


# 方法3 列表解析
d = [i for i in a if i > 5]
print(d)

# 方法4 按索引倒叙删除
for i in range(len(a)-1, -1, -1):  # 从末尾往前挨个
    if i >= 5:
        pass
    else:
        a.remove(a[i])
print(a)
