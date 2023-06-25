# python如何实现单例模式?请写出两种实现方式?
# 方法1 使用装饰器
def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class Foo(object):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)


# 方法2 使用基类
class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Foo(Singleton):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)


# 方法3 使用元类
class Singleton(type):  # type是元类
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=Singleton):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)


