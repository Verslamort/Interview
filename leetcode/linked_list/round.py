class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class circular(object):
    """循环链表"""
    def __init__(self):
        """初始化head指针和链表长度length"""
        self.head = None
        self.length = 0

    def printList(self):
        """打印循环列表中节点的数据项"""
        i = self.length
        ls = []
        temp = self.head
        while i > 0:
            ls.append(temp.data)
            temp = temp.next
            i -= 1
        print(ls)

    def createList(self):
        """创建节点数据为10,8,6,4,2的循环链表"""
        self.head = Node(None, None)  # 哑头节点
        self.head.next = self.head  # 哑头节点的next指向自身
        for count in [2, 4, 6, 8, 10]:
            self.head = Node(count, self.head)
            self.length += 1
        return self.head, self.length

    def insertAnywhere(self, index, newItem):
        """任意位置插入节点"""
        temp = self.head  # 临时指针temp
        while index > 1 and temp.next != None:  # 若0<index<len(linkedlist)-1，搜索索引index处的节点
            temp = temp.next
            index -= 1
        temp.next = Node(newItem, temp.next)  # 插入节点，数据项为newItem， 链接指向下一节点


if __name__ == '__main__':
    cir = circular()
    cir.createList()
    cir.insertAnywhere(1, 100)
    cir.printList()
