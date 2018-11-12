class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = 0
        oldCnt = -1
        for i, n in enumerate(nums):
            if n == 1:
                count += 1
            else:
                ans = max(ans, oldCnt+1+count)
                if i==0 or nums[i-1] == 1:
                    oldCnt = count
                    count = 0
                else:
                    oldCnt = -1
                    count = 0
        ans = max(ans, oldCnt+1+count)
        return ans
