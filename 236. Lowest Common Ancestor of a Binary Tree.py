"""
The solution is bit counter-intuitive. See comments in the code.
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None # yes, of course
        if root == p or root == q:
            return root # yes, but only we assum the tree with this root contains both p and q
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        if leftLCA is not None and rightLCA is not None:
            # here is the counter-intuitive part.
            # why it could happen that both sub-trees are the LCA?
            # the reasons is that the second if condition just checked one p or q,
            # so it may happen.
            # in this case return root
            return root
        else:
            return leftLCA if rightLCA is None else rightLCA # yes, of course
