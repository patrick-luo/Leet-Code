class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isNum(c):
            return '0' <= c <= '9'
        
        def isInt(s, sign):
            """ Check if 's' is an integer.
            
            'sign' is an indicator saying if permitting
            the starting sign ('+' or '-') or not.
            """
            if len(s) == 0:
                return False
            for si in s[1:]:
                if not isNum(si):
                    return False
            return isNum(s[0]) or sign and len(s)>=2 and (s[0]=='+' or s[0]=='-')
        
        def isFloat(s):
            """Check if 's' could be a general float number.
            
            Assum it there's a dot.
            """
            if len(s) == 0:
                return False
            nums = s.split('.')
            if len(nums) == 1:
                return isInt(nums[0], True)
            elif len(nums) == 2:
                return (nums[0] in ('','+','-') or isInt(nums[0], True)) and isInt(nums[1], False) \
                    or (isInt(nums[0], True) and nums[1]=='') # the last 'or' for case '4.'
            else:
                return False
        
        # Main function here
        # First, skip the starting and ending spaces
        # equivalent to s = s.strip()
        i, j = 0, len(s)
        while i<j and s[i] == ' ':
            i += 1
        while i<j and s[j-1] == ' ':
            j -= 1
        if i < j:
            s = s[i:j]
        else:
            return False
        
        # Then assum it may have an 'e'
        nums = s.split('e')
        if len(nums) == 1:
            return isFloat(nums[0])
        elif len(nums) == 2:
            return isFloat(nums[0]) and isInt(nums[1], True)
        else:
            return False
        
        
