ll = [1, 2, 3]
d = dict(a=1)  # {a: 1}

print(type(ll))
print(type(d))

print(isinstance(ll, list))
print(isinstance(d, dict))


def add(a, b):
    if isinstance(a, int):
        return a + b
    elif isinstance(a, str):
        return a.upper() + b


print(add(1, 2))
print(add('head', 'tail'))


print(id(ll))
print(id(d))
print(ll is d)
print(ll is ll)
