class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index = {a: i for i, a in enumerate(A)} # just inversed index
        longest = dict() # key is (i,j), meaning the longest Fibolacci sequence ending with A[i] and A[j]
        
        ans = 0
        for k, a in enumerate(A): 
            for j in xrange(k):
                if a-A[j] in index:
                    i = index[a-A[j]] # A[i]+A[j]=A[k]
                    if i < j:
                        prev = longest[i,j] if (i,j) in longest else 2
                        longest[j, k] = prev + 1
                        ans = max(ans, longest[j, k])
                    
        return ans
