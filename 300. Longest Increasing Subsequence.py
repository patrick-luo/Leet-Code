class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bsearch(seq, target, lo, hi):
            while lo <= hi:
                mid = lo + (hi-lo)/2
                if seq[mid] == target:
                    return mid
                elif seq[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo
        
        # this list stores the past increasing sub-sequence
        # 0 doesn't matter here, just to init a size-n list
        subSeq = [0] * len(nums)
        maxLen = 0
        for ni in nums:
            loc = bsearch(subSeq, ni, 0, maxLen-1)
            subSeq[loc] = ni # now here, the longest sequence including current ni is subSeq[0...loc]
            maxLen = max(maxLen, loc+1)
        return maxLen
