# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            node = self.inorderSuccessor(root.left, p)
            return root if node is None else node