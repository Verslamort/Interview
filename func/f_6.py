# map函数和reduce函数
from functools import reduce

# map
a = [1, 2, 3, 4]
print(map(lambda x: x * x, [1, 2, 3, 4]))
# 用a中的元素调用函数lambda，返回包含每次 function 函数返回值的新列表


# reduce
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))  # ((1*2)*3)*4
