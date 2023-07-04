class Node(object):
    """定义双向链表节点类"""
    def __init__(self, data, previous=None, next=None):
        """data为数据项，previous为上一节点的链接，初始化节点默认链接为None，next为下一节点的链接，初始化节点默认链接为None"""
        self.data = data
        self.next = next
        self.previous = previous


class doubleLinkedList(object):
    """定义双向链表"""
    def __init__(self):
        self.head = None
        self.length = 0

    def traversalReverseOrder(self):
        """创建并反向遍历节点数据项为2,4,6,8,10的双向链表"""
        self.head = Node(2)  # 初始化head节点，数据项为2，previous和next都为None
        self.length += 1
        tail = self.head  # 结尾链接为self.head
        for data in [4, 6, 8, 10]:  # 向单节点双链表的末尾依次插入数据项为4，6,8,10的新节点
            tail.next = Node(data, tail)  # 新节点的previous指向尾节点，尾节点的next指针指向新节点
            tail = tail.next  # tail指针指向新节点
            self.length += 1
        temp = tail
        while temp != None:  # temp不为None时，反向遍历链表
            print(temp.data)
            temp = temp.previous  # 获取temp前一个节点的数据项


if __name__ == '__main__':
    d = doubleLinkedList()
    d.traversalReverseOrder()
