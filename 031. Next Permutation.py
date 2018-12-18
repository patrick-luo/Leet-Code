class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        else:
            nums.sort()
            return
        
        for j in xrange(i+1, len(nums)):
            if nums[j] <= nums[i]:
                break
        else:
            j += 1
        nums[i], nums[j-1] = nums[j-1], nums[i]
        nums[i+1:] = sorted(nums[i+1:])
        
