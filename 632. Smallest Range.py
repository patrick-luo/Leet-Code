class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        def smaller(p, q):
            return (p[1]-p[0])<(q[1]-q[0]) or \
                (p[1]-p[0])==(q[1]-q[0]) and p[0]<q[0]
        
        minR = [sys.float_info.max, -sys.float_info.max]
        pq = list()
        for array in nums:
            heapq.heappush(pq, (array[0], array, 0))
            minR[0] = min(minR[0], array[0])
            minR[1] = max(minR[1], array[0])
        curR = [minR[0], minR[1]]
        
        while True:
            val, array, i = heapq.heappop(pq)
            if i == len(array)-1:
                return minR
            else:
                heapq.heappush(pq, (array[i+1], array, i+1))
                curR[1] = max(curR[1], array[i+1])
                curR[0] = pq[0][0]
                if smaller(curR, minR):
                    minR[0] = curR[0]
                    minR[1] = curR[1]
