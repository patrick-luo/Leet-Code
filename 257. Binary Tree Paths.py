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
        def dfs(res, nodes, root):
            if root is None:
                return
            nodes.append(root)
            if root.left is None and root.right is None:
                res.append(getPath(nodes))
            else:
                dfs(res, nodes, root.left)
                dfs(res, nodes, root.right)
            nodes.pop()
        
        def getPath(nodes):
            path = str(nodes[0].val)
            for n in nodes[1:]:
                path += '->' + str(n.val)
            return path
                
        
        res = list()
        nodes = list()
        dfs(res, nodes, root)
        return res
