# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def findMax(nums):
            idx, m = 0, nums[0]
            for i,ni in enumerate(nums):
                if ni > m:
                    idx, m = i, ni
            return idx, m
        
        if len(nums) == 0:
            return None
        idx, m = findMax(nums)
        root = TreeNode(m)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[(idx+1):])
        return root
