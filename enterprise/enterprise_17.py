# 两个有序列表，l1,l2，对这两个列表进行合并不可使用extend
def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:  # 每次比较第一个元素
            tmp.append(l1[0])  # 小的放进新列表
            del l1[0]  # 删除原有第一个
        else:
            tmp.append(l2[0])
            del l2[0]
    # 一个列表添加完，继续添加另一个列表
    while len(l1) > 0:
        tmp.append(l1[0])
        del l1[0]
    while len(l2) > 0:
        tmp.append(l2[0])
        del l2[0]
    return tmp


if __name__ == '__main__':
    L1 = [1, 4, 7, 11, 24, 32]
    L2 = [3, 6, 10, 22, 29, 41]
    # l3 = loop_merge_sort(L1, L2)
    # print(l3)

    # 法2
    l4 = L1 + L2
    l4.sort()
    print(l4)
