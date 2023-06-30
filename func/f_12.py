# 面向对象中怎么实现只读属性?

# 将对象私有化，通过公有方法提供一个读取数据的接口
class Person:
    def __init__(self):
        self.__name = 'leo'  # 私有化

    def get_name(self):  # 方法
        return self.__name


p = Person()
print(p.get_name())


# 使用装饰器
class MyAge(object):
    def __init__(self):
        self.__age = 23

    @property  # 装饰器property实现只读， 把方法当做属性来使用
    def __getAge__(self):
        return self.__age


m = MyAge()
print(m.__getAge__)


