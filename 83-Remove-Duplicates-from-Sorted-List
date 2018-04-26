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
        curr = head
        while curr is not None:
            p = curr.next
            while p is not None and p.val == curr.val:
                p = p.next
            curr.next = p
            curr = p
        return head
