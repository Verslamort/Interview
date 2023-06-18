class MyException(Exception):
    pass


try:
    raise MyException('my exception')
except MyException as e:
    print(e)
