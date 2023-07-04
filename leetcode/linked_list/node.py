class Node(object):
    """定义单链表节点类"""
    def __init__(self, data, next=None):
        """data为数据项目， next为下一节点的链接， 初始化节点默认链接为None"""
        self.data = data
        self.next = next


class linkedList(object):
    """定义一个单链表类"""
    def __init__(self):
        """初始化head指针和链表的长度length"""
        self.head = None
        self.length = 0

    def demo(self):
        """链表的演示"""
        node1 = Node  # 没有指向节点对象
        node2 = Node(1, None)  # 数据项为1，链接为空的节点
        node3 = Node('hello', node2)  # 数据为hello，链接指向node2的节点
        print(node1, node2.data, node2, node3.next)

    def createLinkedList(self):
        """创建含有5个节点，数据项分别为10,8,6,4,2的链表"""
        for count in [2, 4, 6, 8, 10]:
            self.head = Node(count, self.head)
            self.length += 1  # 每增加一个节点，链表长度length+1
        return self.head, self.length  # 返回链表和链表长度

    def printLinkedList(self):
        i = self.length
        ls = []
        temp = self.head
        while i > 0:
            ls.append(temp.data)  # 向列表中添加节点数据项
            temp = temp.next
            i -= 1
        print(ls)

    def traversal(self):
        """遍历链表"""
        head = None  # 将head定义为None
        for count in range(1, 6):  # 创建5个节点，数据项为5,4,3,2,1
            head = Node(count, head)
        while head != None:  # 若head非空
            print(head.data)  # 打印节点数据项
            head = head.next

    def searchTarget(self, targetItem):
        """搜索某个目标值"""
        temp = self.head
        while temp != None and targetItem != temp.data:  # 若temp不为None且temp.data ！= 6进入循环
            temp = temp.next
        if temp != None:
            print(targetItem, 'has been found')
        else:
            print(targetItem, 'is not in linkedlist')

    def searchIndex(self, index):
        """访问链表某一项"""
        temp = self.head  # 临时指针变量temp初始化为head指针
        while index > 0:  # 顺序查找指定索引的节点的数据项
            temp = temp.next
            index -= 1
        print(temp.data)

    def replaceTarget(self, targetItem, newItem):
        """替换某个目标值"""
        temp = self.head
        while temp != None and targetItem != temp.data:
            temp = temp.next
        if temp != None:
            temp.data = newItem  # 目标值替换为newitem
            print(targetItem, 'has been replaced by', newItem)
        else:
            print(targetItem, 'is not in linkedlist')

    def replaceIndex(self, index, newItem):
        """替换链表某一项"""
        temp = self.head
        while index > 0:  # 顺序查找索引为3的节点的数据项
            temp = temp.next
            index -= 1
        temp.data = newItem  # 将索引为3的数据项替换为100

    def insertAtEnd(self, newItem):
        """在末尾插入元素"""
        if self.head is None:  # 如果head为None，设置head为新节点
            self.head = Node(newItem, self.head)
        else:  # 如果head不为None，搜索最后一个节点，并将next指向新节点
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(newItem, None)
        self.length += 1  # 插入元素，链表长度+1

    def insertAnywhere(self, index, newItem):
        """任意位置插入元素"""
        if self.head is None or index <= 0:  # 如果head为None或者index<=0，在链表开始处插入
            self.head = Node(newItem, self.head)
        else:
            temp = self.head
            while index > 1 and temp.next != None:  # 搜素（index-1）位置处的节点
                temp = temp.next
                index -= 1
            temp.next = Node(newItem, temp.next)  # 在（index-1）节点后插入新节点
        self.length += 1

    def deleteAtEnd(self):
        """在末尾处删除元素"""
        if self.head.next is None:  # 如果链表中只有一个节点，那么将head设置为None
            self.head = None
        else:
            temp = self.head
            while temp.next.next != None:  # 搜索倒数第二个节点，并把其next设置为None
                temp = temp.next
            removeItem = temp.next.data  # 删除最后一个节点的数据项
            temp.next = None
        self.length -= 1  # 删除完元素，链表长度-1

    def deleteAnywhere(self, index):
        """在任意位置删除元素"""
        if index <=0 or self.head.next is None:  # 删除第一项
            removeItem = self.head.data
            self.head = self.head.next
        else:
            temp = self.head
            while index > 1 and temp.next.next != None:  # 搜索第index-1或倒数第二项
                temp = temp.next
                index -= 1
            removeItem = temp.next.data
            temp.next = temp.next.next
        self.length -= 1


if __name__ == '__main__':
    l = linkedList()
    l.createLinkedList()
    print('----')
    l.searchTarget(6)
    l.searchIndex(3)
    print('----')
    l.replaceTarget(6, 100)
    l.printLinkedList()
    print('----')
    l.replaceIndex(2, 100)
    l.printLinkedList()
    print('----')
    l.insertAtEnd(100)
    l.printLinkedList()
    print('----')
    l.insertAnywhere(2, 200)
    l.printLinkedList()
    print('----')
    l.deleteAtEnd()
    l.printLinkedList()
    print('----')
    l.deleteAnywhere(3)
    l.printLinkedList()




