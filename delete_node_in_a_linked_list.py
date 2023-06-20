class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead
        """
        nextnode = node.next
        after_next_node = node.next.next
        node.val = nextnode.val
        node.next = after_next_node
