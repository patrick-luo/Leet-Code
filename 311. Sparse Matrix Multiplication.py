class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        def getNonEmptyA(A):
            a = dict()
            for i, row in enumerate(A):
                for j, elem in enumerate(row):
                    if elem != 0:
                        if i not in a:
                            a[i] = dict()
                        a[i][j] = elem
            return a
        
        def getNonEmptyB(B):
            b = dict()
            for i, row in enumerate(B):
                for j, elem in enumerate(row):
                    if elem != 0:
                        if j not in b:
                            b[j] = dict()
                        b[j][i] = elem
            return b
        
        def initC(m, n):
            C = list()
            for i in xrange(m):
                C.append([0]*n)
            return C
        
        if len(A) == 0 or len(A[0]) == 0:
            return list()
        if len(B) == 0 or len(B[0]) == 0:
            return list()
        a = getNonEmptyA(A)
        b = getNonEmptyB(B)
        C = initC(len(A), len(B[0]))
        for i in a:
            for j in b:
                for k in a[i]:
                    if k in b[j]:
                        C[i][j] += a[i][k]*b[j][k]
                        
        return C
