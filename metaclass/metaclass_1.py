# 遍历一个object的所有属性，并print每一个属性名？
class car:
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize

    def get_name(self):
        return self.name

    def get_prize(self):
        return self.prize


if __name__ == '__main__':
    Lamborghini = car('兰博基尼', 300)
    print(getattr(Lamborghini, 'name'))
    print(getattr(Lamborghini, 'prize'))
    print(dir(Lamborghini))
