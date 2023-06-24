# 给定两个列表，怎么找出他们相同的元素和不同的元素？
list1 = [1, 2, 3]
list2 = [3, 4, 5]
a = [x for x in list1 if x in list2]
print('相同元素为：')
print(a)
b = [y for y in (list1 + list2) if y not in a]
print('不同元素为：')
print(b)

# 使用集合，位运算符
set1 = set(list1)
set2 = set(list2)
print('相同元素为：')
print(set1 & set2)
print('不同元素为：')
print(set1 ^ set2)
