"""They key idea is to sort nums first (the time
complexity will be > nlogn anyway), move the first
index from the begining and then do 2sum for the rest
(using two pointers).

Note: in order to de-duplicate, skip the duplicates
when each pointer is moved. See the comments below.
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        nums.sort()
        for i in xrange(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]: # skip duplicates!
                lo, hi = i+1, len(nums)-1
                while lo < hi:
                    s = nums[i] + nums[lo] + nums[hi]
                    if s < 0:
                        lo += 1
                    elif s > 0:
                        hi -= 1
                    else:
                        res.append([nums[i], nums[lo], nums[hi]])
                        lo += 1
                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo += 1 # skip duplicates!
                        hi -= 1
                        while lo < hi and nums[hi] == nums[hi+1]:
                            hi -= 1 # skip duplicates!
        return res
