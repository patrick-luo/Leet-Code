class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)
        prod = 1
        for i, ni in enumerate(nums):
            ans[i] = prod
            prod *= ni
        i = len(nums)-1
        prod = 1
        while i >= 0:
            ans[i] *= prod
            prod *= nums[i]
            i -= 1
        return ans
        
