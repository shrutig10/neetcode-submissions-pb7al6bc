"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # when we add the random pointers, the linked list has to already be built 
        # we will need to iterate through the linked list at least twice
        # one to set up the linked list, add to dictionary
        # second iteration to add the pointers
        # how will we add the random pointers?
        # store the node in a dictionary with the old node as they key

        oldToNew = {}

        cur = head 
        while cur:
            newNode = Node(x=cur.val)
            oldToNew[cur] = newNode
            cur = cur.next
        
        cur = head
        while cur:
            node = oldToNew[cur]
            if cur.next:
                node.next = oldToNew[cur.next]
            if cur.random:
                node.random = oldToNew[cur.random]
            cur = cur.next

        return oldToNew[head] if head else None
            
