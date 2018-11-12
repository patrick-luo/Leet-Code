class Solution(object):
    def firstMissingPositive(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in xrange(len(A)):
            while 0 < A[i] <= len(A) and A[A[i]-1] != A[i]:
                tmp = A[i]
                A[i] = A[tmp-1]
                A[tmp-1] = tmp
                
                # Don't use the following!!!
                # A[i], A[A[i]-1] = A[A[i]-1], A[i]
        
        for i, ai in enumerate(A):
            if ai != i + 1:
                return i + 1
        
        return len(A) + 1
