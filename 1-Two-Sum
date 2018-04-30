class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memo = dict()
        for i,ni in enumerate(nums):
            if (target-ni) in memo:
                return [memo[target-ni], i]
            else:
                memo[ni] = i
