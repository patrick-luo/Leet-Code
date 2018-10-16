# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(root, res, lev):
            if root is None:
                return
            if len(res) == lev:
                res.append(list())
            res[lev].append(root.val)
            dfs(root.left, res, lev+1)
            dfs(root.right, res, lev+1)
            
        res = list()
        dfs(root, res, 0)
        return res
