# 手写一个判断时间的装饰器
import datetime


class TimeException(Exception):
    def __init__(self, exception_info):
        super().__init__()
        self.info = exception_info

    def __str__(self):
        return self.info


def timecheck(func):
    def wrapper(*args, **kwargs):
        if datetime.datetime.now().year == 2023:
            func(*args, **kwargs)
        else:
            raise TimeException('函数已过时')
    return wrapper


@timecheck
def test(name):
    print("Hello {}, 2023 Happy".format(name))


if __name__ == '__main__':
    test('leo')
