"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def bstToList(root):
            if root is None:
                return None, None
            
            lHead, lTail = bstToList(root.left)
            rHead, rTail = bstToList(root.right)
            root.left = lTail
            root.right = rHead
            
            if lHead is None:
                head = root
                root.left = rTail
            else:
                head = lHead
                lTail.right = root
            
            if rHead is None:
                tail = root
                root.right = lHead
            else:
                tail = rTail
                rHead.left = root
                rTail.right = head
            
            head.left = tail
            tail.right = head
            
            return head, tail
        
        head, tail = bstToList(root)
        return head
        
