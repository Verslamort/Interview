# 删除排序链表中重复的元素
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        re = head  # 创建指针
        while re and re.next:
            if re.val == re.next.val:
                re.next = re.next.next  # 跳过重复元素
            else:
                re = re.next
        return head


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(1, ListNode(2)))
    r = Solution().deleteDuplicates(l1)
    while r:
        print(r.val, end='')
        r = r.next
