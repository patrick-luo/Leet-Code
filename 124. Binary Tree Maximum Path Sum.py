# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxSum = -sys.float_info.max
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def selfMax(root):
            if root is None:
                return 0
            lMax = selfMax(root.left)
            rMax = selfMax(root.right)
            lMax = max(0, lMax)
            rMax = max(0, rMax)
            self.maxSum = max(self.maxSum, lMax+rMax+root.val)
            return max(lMax, rMax) + root.val
        
        selfMax(root)
        return self.maxSum
        
