# 一句话解决阶乘函数？
from functools import reduce


print(reduce(lambda x, y: x*y, range(1, 8)))  # 1*2*3*4*%*6*7
