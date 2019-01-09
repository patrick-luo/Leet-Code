# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = -sys.float_info.max
        
        def maxSumRoot(root):
            if root is None:
                return 0
            lMax = maxSumRoot(root.left)
            rMax = maxSumRoot(root.right)
            self.maxSum = max(self.maxSum, root.val+max([0,lMax,rMax,lMax+rMax]))
            return root.val + max([0,lMax,rMax])
        
        maxSumRoot(root)
        return self.maxSum
        
