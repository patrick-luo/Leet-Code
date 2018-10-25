# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        p = None
        q = head
        r = head.next
        while True:
            q.next = p
            if r is None:
                return q
            p, q, r = q, r, r.next
            
