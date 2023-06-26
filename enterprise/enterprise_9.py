# 字符串 "123" 转换成 123 ，不使用内置api，例如 int()
# 1 使用str函数
from functools import reduce


def first(s):
    num = 0
    for v in s:
        for j in range(10):
            if v == str(j):
                num = num * 10 + j  # 往前挪一位
    return num


# 2 使用ord函数
def second(s):
    num = 0
    for v in s:
        num = num * 10 + ord(v) - ord('0')
    return num


# 3 在第二种基础用reduce
def third(s):
    return reduce(lambda num, v: num * 10 + ord(v) - ord('0'), s, 0)


# 4 使用eval函数
def forth(s):
    num = 0
    for v in s:
        t = '%s * 1' % v
        n = eval(t)
        num = num * 10 + n
    return num


if __name__ == '__main__':
    s = '123'
    print(first(s))
    print(second(s))
    print(third(s))
    print(forth(s))
