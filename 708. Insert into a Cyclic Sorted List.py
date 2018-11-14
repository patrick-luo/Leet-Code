"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        node = Node(insertVal, None)
        if head is None:
            node.next = node
            return node
        p = head
        largest = head
        while True:
            if p.val > largest.val:
                largest = p
            if p.val <= insertVal <= p.next.val:
                node.next = p.next
                p.next = node
                return head
            else:
                p = p.next
            if p == head:
                break
        node.next = largest.next
        largest.next = node
        return head
