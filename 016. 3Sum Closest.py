"""The idea is the same as problem #15"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best, diff = None, sys.float_info.max
        for i in xrange(len(nums)-2):
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s == target:
                    return s
                elif s < target:
                    lo += 1
                else:
                    hi -= 1
                if abs(target-s) < diff:
                    best, diff = s, abs(target-s)
        return best
