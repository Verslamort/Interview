# 设计实现遍历目录与子目录，抓取.pyc文件
import os
from glob import iglob


# 方法1 使用os.walk
def get_files(dir, suffix):  # 目录，后缀
    res = []
    for root, dirs, files in os.walk(dir):  # 遍历目录
        for filename in files:
            name, suf = os.path.splitext(filename)  # 分离文件名与扩展名
            if suf == suffix:
                res.append(os.path.join(root, filename))
    print(res)


get_files('./', '.pyc')


# 方法2 递归
def pick(obj):
    if obj.endswith('.pyc'):  # 后缀为.pyc
        print(obj)


def scan_path(ph):
    file_list = os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(obj):  # 是否为文件
            pick(obj)
        elif os.path.isdir(obj):  # 是否为目录
            scan_path(obj)


# 方法3 使用glob模块
def func(fp, postfix):
    for i in iglob(f"{fp}/**/*{postfix}", recursive=True):
        print(i)


if __name__ == '__main__':
    path = input('输入目录')
    scan_path(path)
    print('--------')
    postfix = '.pyc'
    func('D:/python_work/pythonProject_interview', postfix)




