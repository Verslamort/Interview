"""
输入链表，将链表值从尾到头返回一个Arraylist
"""


class ListNode(object):
    """创建生成链表节点的类"""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):
    """从尾到头打印单链表"""
    def printLinkedList(self, listNode):
        if not listNode:  # 如果链接为None，返回[]
            return []

        result = []
        while listNode:  # 链表非空
            result.insert(0, listNode.val)  # 在列表第一项插入节点的数据项
            listNode = listNode.next  # 将节点的链接指向下一节点
        return result


if __name__ == '__main__':
    listNode = None
    for i in range(3, 0, -1):  # 定义数据项为[1, 2, 3]的链表
        listNode = ListNode(i, listNode)
    s = Solution()
    print(s.printLinkedList(listNode))
