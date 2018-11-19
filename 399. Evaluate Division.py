class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        parent = dict() # key=node, value=root
        ratio = dict() # key=node, value*node=root
        
        def union(parent, ratio, k, a, b):
            if a not in parent:
                parent[a] = a
                ratio[a] = 1.0
            if b not in parent:
                parent[b] = b
                ratio[b] = 1.0
            pa, ka = find(parent, ratio, a)
            pb, kb = find(parent, ratio, b)
            parent[pb] = pa
            ratio[pb] = k * ka / kb
            
        def find(parent, ratio, a):
            if a not in parent:
                return None, None
            if parent[a] != a:
                root, k = find(parent, ratio, parent[a])
                parent[a] = root
                ratio[a] *= k
            return parent[a], ratio[a]
        
        for eq, var in zip(equations, values):
            union(parent, ratio, var, *eq)
            
        ans = list()
        for q in queries:
            pa, ka = find(parent, ratio, q[0])
            pb, kb = find(parent, ratio, q[1])
            if pa is None or pb is None or pa != pb:
                ans.append(-1.0)
            else:
                ans.append(kb/ka)
        return ans
