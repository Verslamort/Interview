# 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
a = 'k:1 | k1:2 | k2:3| k3:4'
new_dict = {}
c = []
for i in a.split('|'):
    c.append(i.split(':'))
print(c)


def str_to_dict(c):
    for e in c:
        new_dict.update({e[0]: int(e[1])})
    return new_dict


if __name__ == '__main__':
    result = str_to_dict(c)
    print(result)

# 方法2
dict1 = {k: int(v) for k, v in map(lambda x: x.split(':'), a.split('|'))}
print(dict1)

