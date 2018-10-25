class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        memo = {0:-1} # key is the continuous sum from the beginning to nums[i], value is the smallest such 'i'
        maxLen = 0
        ssum = 0
        for i, ni in enumerate(nums):
            ssum += ni
            if (ssum-k) in memo:
                maxLen = max(maxLen, i-memo[ssum-k])
            if ssum not in memo:
                memo[ssum] = i
        return maxLen
            
