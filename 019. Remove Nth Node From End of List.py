# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        q = head
        for i in xrange(n):
            q = q.next
        while q is not None:
            p = p.next
            q = q.next
        p.next = p.next.next
        return dummy.next
