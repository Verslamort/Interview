# 下面这段代码的输出结果将是什么？请解释。
def multipliers():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in multipliers()])
print(multipliers())
"""
    上述问题产生的原因是python闭包的延迟绑定。这意味着内部函数被调用时，参数的值在闭包内进行查
    找。因此，当任何由multipliers()返回的函数被调用时,i的值将在附近的范围进行查找。那时，不管返回
    的函数是否被调用，for循环已经完成，i被赋予了最终的值3.
"""


# [0, 2, 4, 6]
def multipliers2():
    for i in range(4):
        yield lambda x: i * x


print([m(2) for m in multipliers2()])


def multipliers3():
    return [lambda x, i=i: i*x for i in range(4)]


print([m(2) for m in multipliers3()])




