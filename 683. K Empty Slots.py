class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days =[0] * len(flowers)
        for d, loc in enumerate(flowers, 1):
            days[loc-1] = d
            
        ans = sys.float_info.max
        left, right = 0, k+1
        while right < len(days):
            for i in xrange(left+1, right):
                # If there is some middle flower that has
                # bloomed before the two edge flowers
                if days[i] < max(days[left], days[right]):
                    left, right = i, i+k+1
                    break
            else:
                # Find the smallest such day
                ans = min(ans, max(days[left], days[right]))
                # Completely start with a new window
                left, right = right, right+k+1
        return -1 if ans==sys.float_info.max else ans
