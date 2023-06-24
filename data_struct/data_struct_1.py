# 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
def sort_dict(d):
    new_dict = {}
    list_a = []
    # 键值对放进list_a
    for k, v in d.items():
        list_a.append((k, v))
    # list_a 排序
    list_a.sort(key=lambda e: e[1])
    # 将数据更新到新字典
    for e in list_a:
        new_dict.update({e[0]: e[1]})
    return new_dict


if __name__ == '__main__':
    d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
    result = sort_dict(d)
    print(result)

    # 命名使用
    lambda_add = lambda x: x + 10
    print(lambda_add(5))

    # 打印列表中的奇数
    numbers = [1, 12, 37, 43, 51, 62, 83, 43, 90, 2023]
    print(list(filter(lambda x: x % 2 == 1, numbers)))  # filter(判断函数， 可迭代对象)
    # 另一种方案
    new_numbers = [i for i in numbers if i % 2 == 1]
    print(new_numbers)

    # 赋予 'key' 参数
    leaders = ["Warren Buffett", "Yang Zhou", "Tim Cook", "Elon Musk"]
    # 按名字长度把列表排序
    leaders.sort(key=lambda x: len(x))
    print(leaders)
