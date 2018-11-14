The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.

Example 1: 

Given buf = "abc"
read("abc", 1) // returns "a"
read("abc", 2); // returns "bc"
read("abc", 1); // returns ""
Example 2: 

Given buf = "abc"
read("abc", 4) // returns "abc"
read("abc", 1); // returns ""


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
        
