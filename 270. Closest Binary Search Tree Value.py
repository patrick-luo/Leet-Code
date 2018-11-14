Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def bsearch(root, t):
            if root is None:
                return
            if self.ans is None or abs(root.val-t) < abs(self.ans-t):
                self.ans = root.val
            if root.val == t:
                return
            elif root.val < t:
                bsearch(root.right, t)
            else:
                bsearch(root.left, t)
        
        self.ans = None
        bsearch(root, target)
        return self.ans
