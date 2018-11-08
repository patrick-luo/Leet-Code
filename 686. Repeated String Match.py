class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) == 0:
            return 1 if len(B) == 0 else -1
        k = len(B)/len(A) if len(B)%len(A) == 0 else len(B)/len(A)+1
        cand = ''.join([A]*k)
        if B in cand:
            return k
        else:
            cand += A
            if B in cand:
                return k + 1
        return -1
