# 有一个jsonline格式的文件file.txt大小约为10K
# 方法1
from mmap import mmap

from Tools.scripts.finddiv import process


def get_lines(fp):
    # with open('file.txt', 'rb') as f:
    #     return f.readlines()
    """
        现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不
        变的情况下，应该如何实现？需要考虑的问题都有那些？
    """
    # with open('file.txt', 'rb') as f:
    #     for i in f:
    #         yield i
    # 是设置下每次返回的行数较好，否则读取次数太多。
    # l = []
    # with open('file.txt', 'rb') as f:
    #     data = f.readlines(100)
    # l.append(data)
    # yield l
    with open(fp, "r+") as f:
        m = mmap(f.fileno(), 0)
    tmp = 0
    for i, char in enumerate(m):
        if char == b"\n":
            yield m[tmp:i + 1].decode()
    tmp = i + 1


if __name__ == '__main__':
    # for e in get_lines():
    #     process(e)  # 处理每一行数据
    for i in get_lines("file.txt"):
        print(i)


