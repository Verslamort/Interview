# 统计一段字符串中字符出现的次数
# 方法1
from collections import Counter


def count(str):
    a = {}
    for s in str:
        a[s] = a.get(s, 0) + 1
    return a


if __name__ == '__main__':
    e = 'AABBBBCCD'
    print(count(e))
    # 方法2
    str_count_data = ""  # 定义空字符串
    for k, v in count(e).items():  # 将键值对转换成字符串相加与空字符串拼接
        str_count_data += k + str(v)
    print(str_count_data)

    # 方法3 使用Counter中的most_common
    print("".join(map(lambda x: x[0] + str(x[1]), Counter(e).most_common())))

