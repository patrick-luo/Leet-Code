# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        l = self.mergeKLists(lists[:len(lists)/2])
        r = self.mergeKLists(lists[len(lists)/2:])
        head = ListNode(None)
        p = head
        while l is not None and r is not None:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l if r is None else r
        return head.next
