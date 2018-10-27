class Solution(object):
    mapping = {'2':'abc', '3': 'def', '4':'ghi',\
              '5':'jkl', '6':'mno', '7': 'pqrs', '8':'tuv', '9':'wxyz'}
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return list()
        letters = Solution.mapping[digits[0]]
        if len(digits) == 1:
            return [let for let in letters]
        combos = self.letterCombinations(digits[1:])
        res = list()
        for com in combos:
            for let in letters:
                res.append(let+com)
        return res
        
