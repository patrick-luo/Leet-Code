# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.s = 0
        def dfs(node, is_left):
            if node:
                if not node.left and not node.right and is_left:
                    self.s += node.val
                else:
                    dfs(node.left, True)
                    dfs(node.right, False)
        
        dfs(root, False)
        return self.s
        
