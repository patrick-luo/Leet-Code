"""One sample solution"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        maxNum = 0
        for ni in nums:
            if ni == 1:
                cnt += 1
            else:
                maxNum = max(maxNum,cnt)
                cnt = 0
        return max(maxNum,cnt)
