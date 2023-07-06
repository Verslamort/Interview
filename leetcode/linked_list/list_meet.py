# 相交链表
"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 算出链表距离差挨个对比
class Solute:
    def getIntersectionNode(self, headA, headB):
        cur1 = headA
        cur2 = headB
        n = 0  # 长链先走n步
        while cur1:
            n += 1
            cur1 = cur1.next
        while cur2:
            n -= 1
            cur2 = cur2.next
        if cur1 != cur2:
            return None
        cur1 = headA if n > 0 else headB
        cur2 = headB if cur1 == headA else headA
        n = abs(n)
        while n:
            n -= 1
            cur1 = cur1.next
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1


class Solution(object):
    def listCross(self, headA, headB):
        A = headA
        B = headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(6, ListNode(7)))))
    l2 = ListNode(4, ListNode(5, ListNode(6, ListNode(7))))
    res = Solution().listCross(l1, l2)
    print(res)
    r = Solute().getIntersectionNode(l1, l2)
    print(r)

