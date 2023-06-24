# 请反转字符串 "aStr"?
from functools import reduce

print('aStr'[::-1])


# plan b
def reverse_string(a):
    b = ''
    for i in a:
        b = i + b
    return b


# plac c
print(''.join(reversed('aStr')))
# plan d 使用reduce
print(reduce(lambda x, y: y + x, 'aStr'))


if __name__ == '__main__':
    a = 'aStr'
    result = reverse_string(a)
    print(result)

