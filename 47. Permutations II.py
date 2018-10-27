class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        res = list()
        used = {ni:False for ni in nums}
        for i, ni in enumerate(nums):
            if not used[ni]:
                for combo in self.permuteUnique([nj for j, nj in enumerate(nums) if j!=i]):
                    res.append([ni] + combo)
                used[ni] = True
        return res
