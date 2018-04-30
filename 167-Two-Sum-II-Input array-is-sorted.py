"""The key idea is to have pointers from
the front and rear and then move them to
the middle."""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0, len(numbers)-1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return [i+1, j+1]
