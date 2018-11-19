"""A union find solution"""

class DSU(object):
    def __init__(self, numNodes):
        self.parent = range(numNodes)
        # rank means that we choose the leader 
        # that has a higher following to pick up a new follower
        self.rank = [0] * numNodes
        
    def naiveFind(self, n):
        while self.parent[n] != n:
            n = self.parent[n]
        return n
        
    # This one has the same functionality as naiveFind,
    # but it has a better performance because of 'path compression'
    # Basically, as we compute the correct leader for n,
    # we should remember our calculation.
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    # Return union successful or not.
    # False means they are already connected
    def union(self, m, n):
        mp = self.find(m)
        np = self.find(n)
        if mp == np:
            return False
        
        if self.rank[mp] != self.rank[np]:
            # pick the node with higher rank to be leader
            leader = np if self.rank[mp] < self.rank[np] else mp
            follower = mp if np == leader else np
            self.parent[follower] = leader
            self.rank[leader] += self.rank[follower]
        else:
            self.parent[mp] = np
            self.rank[np] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dsu = DSU(1001)
        for link in edges:
            if not dsu.union(*link):
                return link






"""A DFS solution"""

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
