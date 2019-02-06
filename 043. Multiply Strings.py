class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = [0] * (len(num1)+len(num2))
        for i in xrange(len(num1)-1, -1, -1):
            for j in xrange(len(num2)-1, -1, -1):
                mul = (ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0'))
                ssum = mul + ans[i+j+1]
                ans[i+j] += ssum / 10
                ans[i+j+1] = ssum % 10

        res = list()
        for n in ans:
            if not (len(res)==0 and n==0):
                res.append(str(n))
        return '0' if len(res)==0 else ''.join(res)
