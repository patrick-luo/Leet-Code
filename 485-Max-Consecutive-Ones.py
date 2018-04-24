"""My original solution"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = -1
        maxNum = 0
        inside = False
        for i, ni in enumerate(nums):
            if inside and ni == 0:
                maxNum = max(maxNum, i-start)
                inside = False
            if not inside and ni == 1:
                start = i
                inside = True
        if inside:
            maxNum = max(maxNum, i-start+1)
        return maxNum
        
