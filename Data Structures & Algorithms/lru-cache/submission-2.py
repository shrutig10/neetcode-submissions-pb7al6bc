class Node():
    def __init__(self, key=-1, val=0, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # key value pair --> hashmap
        # noting down usage --> array is O(n) time; use a linkedlist/queue instead
        # remove from the beg, add to the end
        # for the linked list, would need to be doubly linked so you could run o(1) time
        # a normal linked list would require you to iterate through the list to find the node/prev
        # in the hashmap, store the node itself
        # would need to keep track of my head and tail 
        self.capacity = capacity
        self.mapping = {}
            
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.mapping:
            curNode = self.mapping[key]
            curNode.prev.next = curNode.next
            curNode.next.prev = curNode.prev

            curNode.prev = self.tail.prev
            curNode.next = self.tail
            self.tail.prev = curNode
            curNode.prev.next = curNode
            return self.mapping[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            curNode = self.mapping[key]
            curNode.prev.next = curNode.next
            curNode.next.prev = curNode.prev
            del self.mapping[key]

        if len(self.mapping) == self.capacity:
            toRemove = self.head.next
            self.head.next = self.head.next.next
            toRemove.next.prev = self.head
            del self.mapping[toRemove.key]
            
        newNode = Node(key=key, val=value)
        newNode.prev = self.tail.prev
        newNode.prev.next = newNode
        newNode.next = self.tail
        self.tail.prev = newNode
        self.mapping[key] = newNode
        
