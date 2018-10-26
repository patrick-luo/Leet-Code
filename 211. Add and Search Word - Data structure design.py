class Node(object):
    def __init__(self):
        self.next = dict()
        self.stop = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            if c not in p.next:
                p.next[c] = Node()
            p = p.next[c]
        p.stop = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def subSearch(root, word):
            p = root
            for i, c in enumerate(word):
                if c in p.next:
                    p = p.next[c]
                elif c == '.':
                    for replace in p.next:
                        if subSearch(p, replace + word[i+1:]):
                            return True
                    return False
                else:
                    return False
            return p.stop
        
        return subSearch(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
