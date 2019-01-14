class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = list()
        self.val2idx = dict()
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val2idx:
            return False
        else:
            self.nums.append(val)
            self.val2idx[val] = len(self.nums)-1
            return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val2idx:
            return False
        else:
            valIdx = self.val2idx[val]
            lastVal = self.nums[-1]
            lastValIdx = self.val2idx[lastVal]
            self.nums[valIdx], self.nums[lastValIdx] = lastVal, val
            self.val2idx[lastVal] = valIdx
            self.nums.pop()
            del self.val2idx[val]
            return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
