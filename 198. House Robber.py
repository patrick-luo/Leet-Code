class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevMax = 0 # the max not robbing the previous house
        currMax = 0 # the max 
        for n in nums:
            temp = currMax
            currMax = max(currMax, prevMax+n)
            prevMax = temp
        return currMax
