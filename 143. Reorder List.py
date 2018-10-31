# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        i, j = head, head
        while True:
            i = i.next
            j = j.next.next
            if j is None or j.next is None:
                break
        stack = list()
        p = i.next
        while p is not None:
            stack.append(p)
            p = p.next
        i.next = None
        p = head
        while len(stack) > 0:
            node = stack.pop()
            node.next = p.next
            p.next = node
            p = node.next
        return
