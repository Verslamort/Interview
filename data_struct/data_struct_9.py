# 请写出一段python代码实现删除list里面的重复元素？
# 用遍历
def delete(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b


if __name__ == '__main__':
    a = [1, 1, 2, 3, 4, 4]
    result = delete(a)
    print(result)

    # 用集合
    c = list(set(a))
    print(c)

    # 用sort方法
    l1 = [1, 1, 2, 3, 4, 4]
    l2 = list(set(l1))
    l2.sort(key=l1.index)  # or   l2 = sorted(set(l1), key = l1.index)
    print(l2)

