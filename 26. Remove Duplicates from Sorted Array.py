class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j, nj in enumerate(nums):
            if j==0 or nj!=nums[j-1]:
                nums[i] = nj
                i += 1
        return i
