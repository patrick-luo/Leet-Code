class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def myReverse(nums, start=0):
            i, j = start, len(nums)-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
        
        if len(nums) <= 1:
            return
        i = len(nums)-1
        while i >= 1:
            if nums[i-1] < nums[i]:
                break
            else:
                i -= 1
        if i==0:
            myReverse(nums)
            return
        best = i
        for j in xrange(i+1, len(nums)):
            if nums[j] > nums[i-1] and nums[j] < nums[best]:
                best = j
        nums[i-1], nums[best] = nums[best], nums[i-1]
        nums[i:] = sorted(nums[i:])
        
