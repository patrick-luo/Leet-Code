"""This solution uses addition repititively
to find largest power n of 2 such that 2**n*b < a.
Then you keep subtracting these multiples of b of
the form 2**i*b for smaller powers until the remainder
is smaller than b. Each time you subtract,
take the previous quotient and multiply by two.
If there is any remaining in the end, 
just multiply them all by 2 iteratively."""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # e.g. a=100, b=3
        a, b = dividend, divisor
        negative = False if (a>0) == (b>0) else True
        a = a if a>0 else -a
        b = b if b>0 else -b
    

        mult = [b]
        c = b
    
        while c + c <= a:
            c += c
            mult.append(c)
        # here len(mult)=6, then n=5, which is the largest n
        # s.t. 2**n*b < a
        # mult = [3,6,12,24,48,96]
    
        # Here is the main step. After getting i's
        # where 2**i*b < a, keeping substracing them
        # from a and add the 2**i to 'out'.
        i = 0
        out = 0
        while a >= b:
            i += 1
            out += out # here is to iteratively calcuate 2**i
            if a >= mult[-i]:
                a -= mult[-i]
                out += 1
        
    
        # If there is any remaining in the end, 
        # keeping finishing the calculation of 2**i
        while i < len(mult):
            out += out
            i += 1
    
        if negative:
            out = -out
        
        if out>2147483647 or out<-2147483648:
            return 2147483647
        else:
            return out
