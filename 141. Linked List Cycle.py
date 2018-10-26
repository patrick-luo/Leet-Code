# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while True:
            if slow is None:
                return False
            slow = slow.next
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            if slow == fast:
                return True
