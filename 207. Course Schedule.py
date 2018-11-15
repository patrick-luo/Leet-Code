class Solution(object):
    def canFinish(self, num, prereq):
        """
        :type num: int
        :type prereq: List[List[int]]
        :rtype: bool
        """
        links = dict()
        for c1, c2 in prereq:
            if c1 not in links:
                links[c1] = set()
            links[c1].add(c2)
            
        def dfsCyclic(links, c1, visited):
            if visited[c1]:
                return True
            visited[c1] = True
            if c1 in links:
                for c2 in links[c1]:
                    if dfsCyclic(links, c2, visited):
                        return True
            visited[c1] = False
            return False
                
            
        visited = [False] * num
        for c in links:
            if dfsCyclic(links, c, visited):
                return False
        return True
