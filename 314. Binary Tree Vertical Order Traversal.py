# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return list()
        
        res = dict()
        queue = [(root, 0)] # 0 is the vertical level
        while len(queue) > 0:
            newQ = list()
            for (node, vlevel) in queue:
                if vlevel not in res:
                    res[vlevel] = [node.val]
                else:
                    res[vlevel].append(node.val)
                if node.left is not None:
                    newQ.append((node.left, vlevel-1))
                if node.right is not None:
                    newQ.append((node.right, vlevel+1))
            queue = newQ
        return [res[vlev] for vlev in sorted(res)]
