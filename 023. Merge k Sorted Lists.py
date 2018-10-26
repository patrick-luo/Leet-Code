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
        head = ListNode(0)
        p = head
        pq = list()
        for l in lists:
            if l is not None:
                heapq.heappush(pq, (l.val, l))
        while len(pq) > 0:
            _, cur = heapq.heappop(pq)
            p.next = cur
            p = p.next
            cur = cur.next
            if cur is not None:
                heapq.heappush(pq, (cur.val, cur))
        return head.next
