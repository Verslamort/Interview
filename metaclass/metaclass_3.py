# Python中如何动态获取和设置对象的属性？
class Parent:
    x = 10


if hasattr(Parent, 'x'):
    print(getattr(Parent, 'x'))
    setattr(Parent, 'x', 3)
print(getattr(Parent, 'x'))
