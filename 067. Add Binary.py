class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a)-1, len(b)-1
        res = list()
        carry = 0
        while i>=0 or j>=0:
            ai = int(a[i]) if i>=0 else 0
            bj = int(b[j]) if j>=0 else 0
            ck = ai+bj+carry
            res.append(str(ck%2))
            carry = ck/2
            i -= 1
            j -= 1
        if carry > 0:
            res.append('1')
        res.reverse()
        return ''.join(res)
