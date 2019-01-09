# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(root, seq, k):
            if len(seq) >= k:
                return
            if root is not None:
                dfs(root.left, seq, k)
                seq.append(root.val)
                dfs(root.right, seq, k)
        
        seq = list()
        dfs(root, seq, k)
        return seq[k-1]
        
