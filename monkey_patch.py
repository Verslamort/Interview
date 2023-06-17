import socket
import select
import time
from gevent import monkey


print(socket.socket)
print('After monkey patch')

monkey.patch_socket()
print(socket.socket)

print(select.select)
monkey.patch_select()
print('After monkey patch')
print(select.select)

print(time.time())


def _time():
    return 1234

time.time = _time

print(time.time())
