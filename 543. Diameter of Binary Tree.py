# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.diam = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def diamWithSelf(root):
            if root is None:
                return 0
            leftDiam = 0 if root.left is None else 1+diamWithSelf(root.left)
            rightDiam = 0 if root.right is None else 1+diamWithSelf(root.right)
            self.diam = max(self.diam, leftDiam+rightDiam)
            return max(leftDiam, rightDiam)
        
        diamWithSelf(root)
        return self.diam
  
