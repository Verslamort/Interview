# 给定一个任意长度数组，实现一个函数
"""
    让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变
    成'1355798642'
"""


# 方法1
def sort(a):
    b = list(map(int, a))
    c = []
    d = []
    for i in b:
        if i % 2 == 1:
            c.append(i)
            c.sort(reverse=False)
        if i % 2 == 0:
            d.append(i)
            d.sort(reverse=True)
    return ''.join(map(str, (c + d)))


# 方法2
def func1(l):
    if isinstance(l, str):  # 如果是字符串，拆分成数字列表
        l = [int(i) for i in l]
    l.sort(reverse=True)  # 降序，偶数不动
    for i in range(len(l)):
        if l[i] % 2 > 0:
            l.insert(0, l.pop(i))  # 奇数从大到小删除后插入列表第一位
    print(''.join(str(e) for e in l))


# 方法3
def func2(l):
    print("".join(sorted(l, key=lambda x: int(x) % 2 == 0 and 20 - int(x) or int(x))))


if __name__ == '__main__':
    a = '1982376455'
    print(sort(a))
    print('----')
    print(func1(a))
    print(func2(a))
