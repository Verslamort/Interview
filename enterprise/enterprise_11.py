# python代码实现删除一个list里面的重复元素
# 1 集合
def first(a):
    a = list(set(a))
    print(a)


# 2 新列表
def second(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(b)


# 3 字典
def third(a):
    c = {}
    c = c.fromkeys(a)  # 以a列表中元素作为键生成新字典
    c = list(c.keys())
    print(c)


if __name__ == '__main__':
    a = [1, 1, 2, 3, 4, 4]
    print(first(a))
    print(second(a))
    print(third(a))
