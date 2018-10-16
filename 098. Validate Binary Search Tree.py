# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isBST(root, lb, ub):
            if root is None:
                return True
            thisRootGood = lb < root.val < ub
            return thisRootGood and isBST(root.left, lb, root.val) \
                and isBST(root.right, root.val, ub)
        return isBST(root, -sys.float_info.max, sys.float_info.max)
