class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ssum = 0
        i = 0
        minLen = sys.float_info.max
        for j, nj in enumerate(nums):
            ssum += nj
            while ssum >= s:
                minLen = min(minLen, j-i+1)
                ssum -= nums[i]
                i += 1
        return 0 if minLen == sys.float_info.max else minLen
            
