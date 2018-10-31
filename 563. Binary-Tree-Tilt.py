"""My solution.

The key idea is to calculate the sum of all
tree nodes and meanwhile record the tilt answer,
avoiding re-calculating things.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def sumTree(self, root, tilt):
        if root is None:
            return 0
        else:
            left = self.sumTree(root.left, tilt)
            right = self.sumTree(root.right, tilt)
            tilt.val += abs(left-right)
            return left + root.val + right
            
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tilt = TreeNode(0)
        self.sumTree(root, tilt)
        return tilt.val
        
