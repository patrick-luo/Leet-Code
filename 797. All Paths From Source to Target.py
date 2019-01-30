class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(graph) == 0:
            return list()
        
        def dfs(graph, start, end):
            if start == end:
                return [[start]]
            ans = list()
            for node in graph[start]:
                for path in dfs(graph, node, end):
                    ans.append([start]+path)
            return ans
        
        return dfs(graph, 0, len(graph)-1)
