class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        res = list()
        for combo in self.subsets(nums[1:]):
            res.append(combo)
            copy = [i for i in combo]
            copy.append(nums[0])
            res.append(copy)
        return res
