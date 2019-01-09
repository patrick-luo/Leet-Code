class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = dict() # <key,val> = <a number, its leftmost index>
        right = dict() # <key,val> = <a number, its rightmost index>
        count = dict() # <key,val> = <a number, its count>
        
        for i, n in enumerate(nums):
            if n not in left:
                left[n] = i
            right[n] = i
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        deg = max(count.values())
        ans = len(nums)
        
        for n in nums:
            if count[n] == deg:
                ans = min(right[n]-left[n]+1, ans)
        return ans
        
