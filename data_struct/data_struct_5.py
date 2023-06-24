# 请按alist中元素的age由大到小排序
alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]


def sort_by_age(list1):
    return sorted(alist, key=lambda x: x['age'], reverse=True)


result = sort_by_age(alist)
print(result)
