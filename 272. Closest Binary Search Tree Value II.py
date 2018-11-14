# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def inorder(root, t, k, ans):
            if root is None:
                return
            
            inorder(root.left, t, k, ans)
            
            if len(ans) < k:
                ans.append(root.val)
            else:
                if t < ans[0] or abs(ans[0]-t) < abs(root.val-t):
                    return
                else:
                    ans.popleft()
                    ans.append(root.val)
            
            inorder(root.right, t, k, ans)
            
        from collections import deque
        ans = deque()
        inorder(root, target, k, ans)
        return ans
