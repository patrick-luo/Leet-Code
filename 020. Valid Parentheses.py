class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'(':')', '[':']', '{':'}'}
        stack = list()
        for si in s:
            if si in ('(', '[', '{'):
                stack.append(si)
            else:
                if len(stack) == 0 or pairs[stack.pop()] != si:
                    return False
        return len(stack) == 0
