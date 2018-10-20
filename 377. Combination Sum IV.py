class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        combo = [1] + [0] * target
        for tar in xrange(1, target+1):
            for ni in nums:
                if ni > tar:
                    break
                elif ni == tar:
                    combo[tar] += 1
                else:
                    combo[tar] += combo[tar-ni]
        return combo[target]
