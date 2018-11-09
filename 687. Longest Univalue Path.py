# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def selfLongestPath(root):
            if root is None:
                return 0
            left = selfLongestPath(root.left)
            right = selfLongestPath(root.right)
            left = left+1 if root.left is not None and root.val==root.left.val else 0
            right = right+1 if root.right is not None and root.val==root.right.val else 0
            self.ans = max(self.ans, left+right)
            return max(left, right)
        
        self.ans = 0
        selfLongestPath(root)
        return self.ans
