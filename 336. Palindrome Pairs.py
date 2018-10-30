class Node(object):
    """It's a Trie node
    
    Node the words are stored reversely
    """
    
    def __init__(self):
        self.next = dict()
        self.stopIdx = -1 # which word[i] stops here (reverse order)
        
        # *****************************************************************
        # which word[i]'s are palindrome here reversely with the left out chars.
        # e.g. word[2] = 'abacd'. Suppose reversely from the root now we
        # have consumed 'd' and 'c', and apparently the left string 'aba'
        # is a palindrome, so we store index i=2 in current node.
        self.palinList = list()

class Solution(object):
    def __init__(self):
        self.root = Node()
        self.ans = list()
        
    def isPalindrome(self, word, i, j):
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True
        
    def add(self, word, i):
        p = self.root
        j = len(word)-1
        while j >= 0:
            if word[j] not in p.next:
                p.next[word[j]] = Node()
            if self.isPalindrome(word, 0, j):
                p.palinList.append(i)
            p = p.next[word[j]]
            j -= 1
        p.palinList.append(i) # for empty left string
        p.stopIdx = i
        
    def search(self, word, i):
        p = self.root
        for j, char in enumerate(word):
            if p.stopIdx>=0 and p.stopIdx!=i and \
                    self.isPalindrome(word, j, len(word)-1):
                self.ans.append([i, p.stopIdx])
            if char in p.next:
                p = p.next[char]
            else:
                return
        for j in p.palinList:
            if j != i:
                self.ans.append([i, j])
                
    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        for i, wi in enumerate(words):
            self.add(wi, i)
        for i, wi in enumerate(words):
            self.search(wi, i)
        return self.ans
    
