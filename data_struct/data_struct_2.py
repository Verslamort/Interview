import random


# 字典推导式
a = [(1, 30), (2, 45), (3, 60)]
b = {key: value for (key, value) in a}
print(b)

# 生成包含四个随机数的字典
random_dict = {i: random.randint(10, 20) for i in range(1, 5)}
print(random_dict)

# 更换字典中的键，值
dict1 = {'1': 'amy', '2': 'bob', '3': 'jack'}
dict2 = {k: v for v, k in dict1.items()}
print(dict1)
print(dict2)
