class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 1:
            return 0
        length = [1] * len(nums) # the max length of increasing subsequence ending at each i
        counts = [1] * len(nums) # the count accordingly
        for i, ni in enumerate(nums):
            for j, nj in enumerate(nums[:i]):
                if nj < ni:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        counts[i] = counts[j]
                    elif length[j] + 1 == length[i]:
                        counts[i] += counts[j]
                else: 
                    pass # doesn't matter because we will check ni with every nj with j<i
        longest = max(length)
        return sum(ci for i, ci in enumerate(counts) if length[i] == longest)
