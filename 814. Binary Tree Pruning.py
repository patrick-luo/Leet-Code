# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            pass
        else:
            left = self.pruneTree(root.left)
            right = self.pruneTree(root.right)
            if root.val == 0 and left is None and right is None:
                root = None
            else:
                root.left = left
                root.right = right
        return root
