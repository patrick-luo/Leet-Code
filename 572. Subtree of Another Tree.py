# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def same_tree(s, t):
            if s == t:
                return True
            if (not s) or (not t):
                return False
            if s.val != t.val:
                return False
            return same_tree(s.left, t.left) \
                and same_tree(s.right, t.right)
        
        if t is None:
            return True
        if s is None:
            return False
        if same_tree(s, t):
            return True
        return self.isSubtree(s.left, t) \
                or self.isSubtree(s.right, t)
        
