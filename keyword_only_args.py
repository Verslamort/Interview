# Feature: Keyword only arguments


def add(a, b, *, c):
    return a + b + c


print(add(1, 2, c=3))
