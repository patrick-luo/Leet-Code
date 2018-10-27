# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(l1, l2):
            head = ListNode(None)
            p = head
            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            p.next = l1 if l2 is None else l2
            return head.next
                    
        def split(head):
            dummy = ListNode(None)
            dummy.next = head
            slow, fast = dummy, dummy
            while True:
                if fast is None or fast.next is None:
                    right = slow.next
                    slow.next = None
                    return dummy.next, right
                else:
                    slow = slow.next
                    fast = fast.next.next
                
        
        if head is None or head.next is None:
            return head
        left, right = split(head)
        sortedLeft = self.sortList(left)
        sortedRight = self.sortList(right)
        return merge(sortedLeft, sortedRight)
        
