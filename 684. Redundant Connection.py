class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = dict()
        
        # dfs search
        # Interpretation: "if one can find 'target' node in current graph.
        # 'node' is the current being checked."
        def find(target, node, graph, visited):
            if node not in visited:
                visited.add(node)
                if node == target:
                    return True
                else:
                    if node in graph:
                        for nei in graph[node]:
                            if find(target, nei, graph, visited):
                                return True
            return False
        
        # The good thing for this loop is that it
        # builds graph and search connectivity simoutaneously
        for u, v in edges:
            visited = set() # 'visited' is super important in undirected graphs!
            if u in graph and v in graph and find(u, v, graph, visited):
                return u, v
            if u not in graph:
                graph[u] = set()
            graph[u].add(v)
            if v not in graph:
                graph[v] = set()
            graph[v].add(u)
