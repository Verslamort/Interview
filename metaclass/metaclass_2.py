# 写一个类，并让它尽可能多的支持操作符?   运算符，分隔符
class Array:
    _list = []

    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destruct')

    def __str__(self):
        return 'this self-defined array class'

    def __getitem__(self, key):
        return self._list[key]

    def __len__(self):
        return len(self._list)

    def Add(self, value):
        self._list.append(value)

    def Remove(self, index):
        del self._list[index]

    def DisplayItems(self):
        print('show all items---')
        for item in self._list:
            print(item)
