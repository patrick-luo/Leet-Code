class Solution(object):
    def canFinish(self, num, prereq):
        """
        :type num: int
        :type prereq: List[List[int]]
        :rtype: bool
        """
        def find(target, node, graph):
            if node == target:
                return True
            else:
                if node in graph:
                    for child in graph[node]:
                        if find(target, child, graph):
                            return True
                return False
        
        graph = dict()
        for c1, c2 in prereq:
            if find(c1, c2, graph):
                return False
            if c1 not in graph:
                graph[c1] = set()
            graph[c1].add(c2)
        return True
