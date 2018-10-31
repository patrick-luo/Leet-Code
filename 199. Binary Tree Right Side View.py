# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = list()
        if root is None:
            return view
        view.append(root.val)
        lView = self.rightSideView(root.left)
        rView = self.rightSideView(root.right)
        view.extend(rView)
        view.extend(lView[len(rView):])
        return view
