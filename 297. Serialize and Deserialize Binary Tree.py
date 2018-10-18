# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, res):
            if node is None:
                res.append('N')
            else:
                res.append(str(node.val))
                dfs(node.left, res)
                dfs(node.right, res)
        
        res = list()
        dfs(root, res) # In-order traversal
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build(nodes):
            num = nodes.popleft()
            if num == 'N':
                return None
            node = TreeNode(int(num))
            node.left = build(nodes)
            node.right = build(nodes)
            return node
        
        nodes = deque(data.split()) #using deque is to use popleft()
        return build(nodes)
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
