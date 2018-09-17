# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Find the max and then break the array in two parts.
# Then recursively  

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def maxTree(nums, start, end):
            if start >= end:
                return None
            else:
                opt = (nums[start], start)
                for i in xrange(start+1, end):
                    if nums[i] > opt[0]:
                        opt = (nums[i], i)
                root = TreeNode(opt[0])
                root.left = maxTree(nums, start, opt[1])
                root.right = maxTree(nums, opt[1]+1, end)
                return root
        
        if nums is None:
            return None
        else:
            return maxTree(nums, 0, len(nums))
