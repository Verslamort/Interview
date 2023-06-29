# hasattr() getattr() setattr() 函数使用详解？

# hasattr
class function_demo(object):
    name = 'demo'

    def run(self):
        return 'hello function'


functiondemo = function_demo()
r = hasattr(functiondemo, 'name')  # 判断对象是否有name属性
e = hasattr(functiondemo, 'run')  # 判断对象是否有run方法
s = hasattr(functiondemo, 'age')  # 判断对象是否有age属性
print(r, e, s)

# getattr
print(getattr(function_demo, 'name'))  # 获取name属性
print(getattr(function_demo, 'run'))  # 获取run方法
print(getattr(function_demo, 'age', 18))  # 获取不存在的属性，返回默认值

# setattr(object, name, values)   给属性赋值， 无则先创建再赋值
setattr(function_demo, 'age', 18)
print(getattr(function_demo, 'age', 18))


# 综合使用
class function_demo2(object):
    name = "demo"

    def run(self):
        return "hello function"


functiondemo1 = function_demo2()
res = hasattr(functiondemo1, 'addr')  # 先判断是否存在
if res:
    addr = getattr(functiondemo1, 'addr')
    print(addr)
else:
    addr = getattr(functiondemo1, 'addr', setattr(functiondemo1, 'addr', '北京首都'))  # 如果没有，将addr创建并赋值北京首都
    print(addr)


