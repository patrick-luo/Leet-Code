# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def flat(root):
            """Return the last node"""
            if root is None:
                return None
            leftEnd = flat(root.left)
            rightEnd = flat(root.right)
            if leftEnd is not None:
                leftEnd.right = root.right
                root.right = root.left
                root.left = None
            if rightEnd is not None:
                return rightEnd
            elif leftEnd is not None:
                return leftEnd
            else:
                return root
        flat(root)
            
