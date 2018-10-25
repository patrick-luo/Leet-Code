class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        writer = 0
        for ni in nums:
            if ni != 0:
                nums[writer] = ni
                writer += 1
        while writer < len(nums):
            nums[writer] = 0
            writer += 1
