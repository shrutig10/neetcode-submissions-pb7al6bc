class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity: int):
        # define a doubly linked list to represent the current use of the nodes
        # define a hashmap to store key value pairs (key --> node)
        # define head and tail to point to the most and least recently node
        # create methods to insert and delete nodes
        self.mapping = {}
        self.cap = capacity
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
         

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        
        self.remove(self.mapping[key])
        self.insert(self.mapping[key])
        return self.mapping[key].val

        
    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])

        node = Node(key, value)
        self.mapping[key] = node
        self.insert(node)

        if len(self.mapping) > self.cap:
            node = self.head.next
            self.remove(self.head.next)
            del self.mapping[node.key]

        
        


        







        