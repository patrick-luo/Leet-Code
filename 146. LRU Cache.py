""" Not sure why 'get' is not working """

class Node(object):
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head
        self.memo = dict()
        self.cap = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if len(self.memo) == 0 or key not in self.memo:
            return -1
        node = self.memo.get(key)
        self.refresh(node)
        return node.val
    
    def refresh(self, node):
        self.delete(node)
        self.add(node)
        
    def add(self, node):
        node.right = self.head.right
        self.head.right = node
        node.right.left = node
        node.left = self.head
        
    def delete(self, node):
        node.left.right = node.right
        node.right.left = node.left
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.memo:
            memo[key].val = value
            self.refresh(memo[key])
        else:
            newNode = Node(key, value)
            self.add(newNode)
            self.memo[key] = newNode
            if len(self.memo) > self.cap:
                self.delete(self.tail.left)
                del self.memo[self.tail.left.val]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
