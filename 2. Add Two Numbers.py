# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p = head
        carry = 0
        while l1 is not None or l2 is not None:
            n1 = 0 if l1 is None else l1.val
            n2 = 0 if l2 is None else l2.val
            ssum = n1 + n2 + carry
            p.next = ListNode(ssum % 10)
            p = p.next
            carry = ssum / 10
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        if carry > 0:
            p.next = ListNode(carry)
        return head.next
