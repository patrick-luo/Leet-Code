# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next is not None:
            p = curr.next
            if p.next is None or p.next.val != p.val:
                curr = p
            else:
                q = p.next
                while q is not None and q.val == p.val:
                    q = q.next
                curr.next = q
        return dummy.next
        
