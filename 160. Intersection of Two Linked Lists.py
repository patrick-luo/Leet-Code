# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa, pb = headA, headB
        while True:
            if pa == pb:
                return pa
            if pa.next is None or pb.next is None:
                break
            pa, pb = pa.next, pb.next
        slow = pa if pa.next is not None else pb
        fast = pb if pa == slow else pa
        count = 0
        while True:
            if slow.next is None:
                break
            slow = slow.next
            count += 1
        if slow != fast:
            return None
        shorter = headA if fast == pa else headB
        longer = headB if shorter == headA else headA
        for i in xrange(count):
            longer = longer.next
        while True:
            if shorter == longer:
                return shorter
            shorter = shorter.next
            longer = longer.next
