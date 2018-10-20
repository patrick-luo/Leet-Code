class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainders = {0:-1}
        subSum = 0
        for i, ni in enumerate(nums):
            subSum += ni
            if k != 0:
                subSum %= k
            if subSum in remainders:
                if i - remainders[subSum] > 1:
                    return True
            else:
                remainders[subSum] = i
        return False
                
                
                
