# 反转链表
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        # 判断当前节点和下一节点是否为None
        if not head:
            return None
        if not head.next:
            print(head.val)
            return head
        headNode = self.reverseList(head.next)  # head.next链表一直往后传递，直到找到最后一个节点
        head.next.next = head
        head.next = None
        return headNode


if __name__ == '__main__':
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = Solution().reverseList(l)
    while res:
        print(res.val, end='')
        res = res.next
