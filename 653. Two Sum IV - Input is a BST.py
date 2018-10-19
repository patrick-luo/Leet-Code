# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



"""The key idea is to use a memo to record visited
values and use a sub-function find() to locate the
other element if applicable.

Note: this solution works for any binary trees
other than a BST."""
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def find(root, k, memo):
            if root is None:
                return False
            if (k-root.val) in memo:
                return True
            memo.add(root.val)
            return find(root.left, k, memo) or find(root.right, k, memo)
        
        memo = set()
        return find(root, k, memo)
