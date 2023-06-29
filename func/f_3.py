# 带参数的装饰器?

# 带定长参数的装饰器
def new_func(func):
    def wrappedfun(username, password):
        if username == 'root' and password == '1234567890':
            print('通过认证')
            print('开始执行附加功能')
            return func()
        else:
            print('用户名或密码错误')
            return
    return wrappedfun


@new_func
def origin():
    print('开始执行函数')


# 带不定长参数的装饰器
def new_func2(func):
    def wrappedfun(*parts):
        if parts:
            counts = len(parts)
            print('本系统包含 ', end='')
            for part in parts:
                print(part, ' ', end='')
            print('等', counts, '部分')
            return func()
        else:
            print('用户名或密码错误')
            return func()
    return wrappedfun


@new_func2
def origin2():
    print('开始执行函数')


if __name__ == '__main__':
    origin('root', '1234567890')
    origin2('root', '1234567890')


