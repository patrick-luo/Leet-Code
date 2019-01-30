class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for n in nums:
            count[n] += 1
        for i in xrange(count[0]):
            nums[i] = 0
        for i in xrange(count[0], count[0]+count[1]):
            nums[i] = 1
        for i in xrange(count[0]+count[1], len(nums)):
            nums[i] = 2
        
