class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.index = dict() # <key,val>=<key,node>
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.right = self.tail
        self.tail.left = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.index:
            return -1
        p = self.index[key]
        self._delete(p)
        self._addHead(p)
        return p.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.index:
            p = self.index[key]
            p.val = value
            self._delete(p)
            self._addHead(p)
        else:
            if len(self.index) == self.cap:
                self.index.pop(self.tail.left.key)
                self._delete(self.tail.left)
            p = Node(key, value)
            self._addHead(p)
            self.index[key] = p
            
    def _delete(self, p):
        q, r = p.left, p.right
        q.right = r
        r.left = q
        p.left, p.right = None, None
        
    def _addHead(self, p):
        q = self.head.right
        self.head.right = p
        p.right = q
        q.left = p
        p.left = self.head
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
