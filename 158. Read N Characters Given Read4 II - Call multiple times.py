""""Not sure why it gives wrong answers"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    
    def __init__(self):
        self.left = list()
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n <= len(self.left):
            buf[:] = self.left[:n]
            self.left = self.left[n:]
            return n
        
        cnt = len(self.left)
        buf[:cnt] = self.left[:]
        tbuf = [''] * 4
        
        while True:
            once = read4(tbuf)
            if cnt+once <= n:
                buf[cnt:cnt+once] = tbuf[:]
                cnt += once
                if once < 4:
                    self.left = list()
                    return cnt
            else:
                buf[cnt:n] = tbuf[:n-cnt]
                self.left = tbuf[n-cnt:]
                return n
        
