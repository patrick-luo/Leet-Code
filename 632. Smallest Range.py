"""Not sure why time limit exceeded
"""

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        def smaller(this, that):
            return (this[1]-this[0]) < (that[1]-that[0]) or \
                (this[1]-this[0]) == (that[1]-that[0]) and this[0] < that[0]
        
        pq = list()
        curR = [sys.float_info.max, -sys.float_info.max]
        for array in nums:
            curR[0] = min(curR[0], array[0])
            curR[1] = max(curR[1], array[0])
            heapq.heappush(pq, (array[0], array, 0))
        minR = [curR[0], curR[1]]
        
        while True:
            val, array, i = heapq.heappop(pq)
            if i < len(array)-1:
                heapq.heappush(pq, (array[i+1], array, i+1))
                curR[0] = heapq.nsmallest(1, pq)[0][0]
                curR[1] = max(curR[1], array[i+1])
                if smaller(curR, minR):
                    minR = [curR[0], curR[1]]
            else:
                return minR
