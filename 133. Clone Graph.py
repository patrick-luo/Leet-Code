# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def clone(node, built):
            if node.label not in built:
                newNode = UndirectedGraphNode(node.label)
                built[node.label] = newNode
                for n in node.neighbors:
                    newNode.neighbors.append(clone(n, built))
            return built[node.label]
        
        if node is None:
            return None
        built = dict()
        return clone(node, built)
        
