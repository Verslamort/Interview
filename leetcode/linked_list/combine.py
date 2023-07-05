# 合并两个有序链表
class ListNode(object):
    """创建生成链表节点的类"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 迭代
class Solute(object):
    def mergeTwoLists(self, list1, list2):
        global num
        res = ListNode()
        re = res
        while list1 and list2:
            # l1, l2是否存在
            num1 = list1.val if list1 else 200
            num2 = list2.val if list2 else 200
            if num1 > num2:
                num = num2
                list2 = list2.next
            elif num1 <= num2:
                num = num1
                list1 = list1.next
            re.next = ListNode(num)
            re = re.next

        while not list1 and list2:
            re.next = ListNode(list2.val)
            list2 = list2.next
            re = re.next

        while not list2 and list1:
            re.next = ListNode(list1.val)
            list1 = list1.next
            re = re.next
        return res.next


# 迭代简化
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # 若一个链表为空，返回另一个
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        # 设置哑节点，始终指向链表头部用于返回整个链表
        res = ListNode()
        re = res
        # 两个链表都不为空，遍历取节点值进行比较
        while list1 and list2:
            if list1.val > list2.val:
                re.next = list2
                # 继续遍历list2，指针指向下一个待比较节点
                list2 = list2.next
            else:
                re.next = list1
                list1 = list1.next
            # 新链表指针指向新节点，用于更新链表
            re = re.next

        # 判断两个链表是否遍历完
        re.next = list1 if list1 else list2
        return res.next  # 返回哑节点后面的链表节点


def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l2.next, l1)
        return l2


if __name__ == '__main__':
    l1 = ListNode(1, (ListNode(2, (ListNode(4)))))
    l2 = ListNode(1, (ListNode(3, (ListNode(4)))))
    rel = Solute().mergeTwoLists(l1, l2)
    res = Solution().mergeTwoLists(l1, l2)
    while rel:
        print(rel.val, end='')
        rel = rel.next
    print('-----')
    while res:
        print(res.val, end='')
        res = res.next
    print(mergeTwoLists(l1, l2))




