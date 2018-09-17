# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, res):
            if root is None:
                return;
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
        
        res = list()
        inorder(root, res)
        return res
