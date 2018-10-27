class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        res = list()
        for i, ni in enumerate(nums):
            for combo in self.permute([nj for j, nj in enumerate(nums) if j!=i]):
                res.append([ni] + combo)
        return res
        
