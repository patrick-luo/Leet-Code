# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        cnt = 0
        tbuf = [''] * 4
        while True:
            once = read4(tbuf)
            if cnt+once <= n:
                buf[cnt:cnt+once] = tbuf[:]
                cnt += once
                if once < 4:
                    return cnt
            else:
                buf[cnt:n] = tbuf[:4-(cnt+once-n)] # (cnt+once-n) is the overflow number
                return n
