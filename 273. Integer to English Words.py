class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        def words(n):
            if n < 20:
                return to19[n-1:n] #n=0 will give an empty list
            elif n < 100:
                return [tens[n/10-2]] + words(n%10)
            elif n < 1000:
                return [to19[n/100-1]] + ['Hundred'] + words(n%100)
            for order, word in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(order+1):
                    return words(n/1000**order) + [word] + words(n%1000**order)
                # e.g. 'Thousand' below:
                # if n < 1000000:
                #     return [words[n/1000]] + ['Thousand'] + words(n%1000)
        return 'Zero' if num==0 else ' '.join(words(num))
