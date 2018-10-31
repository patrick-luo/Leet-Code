class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def findDropIdx(nums):
            i = len(nums) - 1
            while i >= 0:
                if i > 0 and nums[i-1] < nums[i]:
                    return i-1
                else:
                    i -= 1
            return -1
        
        if len(nums) < 2:
            return
        i = findDropIdx(nums)
        if i == -1:
            nums.reverse()
        else:
            for k, nk in enumerate(nums[i+1:], i+1):
                if nk > nums[i]:
                    j = k
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = sorted(nums[i+1:])
