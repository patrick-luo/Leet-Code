# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(root, path, res):
            if root is None:
                return
            path.append(str(root.val))
            if root.left is None and root.right is None:
                res.append('->'.join(path))
            else:
                dfs(root.left, path, res)
                dfs(root.right, path, res)
            path.pop()
        
        res = list()
        dfs(root, list(), res)
        return res
