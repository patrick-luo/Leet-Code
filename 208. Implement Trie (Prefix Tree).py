class Node(object):
    def __init__(self, c=None):
        self.char = c
        self.index = dict()
        self.stop = False
        
    def equalVar(self, c):
        return self.char == c
    
    def containNext(self, c):
        return c in self.index
        
    def getNext(self, c):
        return self.index[c]
    
    def add(self, c):
        self.index[c] = Node(c)
        
    def setStop(self):
        self.stop = True
        
    def isStop(self):
        return self.stop

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for c in word:
            if not curr.containNext(c):
                curr.add(c)
            curr = curr.getNext(c)
        curr.setStop()
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for c in word:
            if not curr.containNext(c):
                return False
            curr = curr.getNext(c)
        return curr.isStop()
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in prefix:
            if not curr.containNext(c):
                return False
            curr = curr.getNext(c)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
