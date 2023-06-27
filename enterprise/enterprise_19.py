# 写一个函数找出一个整数数组中，第二大的数
# 方法1 排序
def search(list):
    new_list = sorted(list, reverse=True)
    print(new_list[1])


# 方法2 设置两个标志位一个存储最大数一个存储次大数
def search_second(num_list):
    one = num_list[0]  # 设置最大数位置
    two = num_list[0]  # 设置第二大数位置
    for i in range(1, len(num_list)):  # 遍历数组
        if num_list[i] > one:  # num大于one时，one的数往后挪一位，num成为新的最大数
            two = one
            one = num_list[i]
        elif num_list[i] > two:  # num大于two上的数，取代其位置
            two = num_list[i]
    print(two)


if __name__ == '__main__':
    a = [21, 423, 45, 63, 232, 15, 26]
    print(search(a))
    print(search_second(a))
