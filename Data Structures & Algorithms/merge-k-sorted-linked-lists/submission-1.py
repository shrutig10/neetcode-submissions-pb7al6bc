# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use a heap
        # each element contains a tuple, (node, index of the list)
        # whichever element is at the top is the least --> take that node from that index
        # if the next node is null, keep it removed from the heap
        # add the next node to the list with the same index
        # make a dummy node, and then add nodes as node.next to the dummy node for the merged list

        head = cur = ListNode()

        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        

        while heap:
            _, i = heapq.heappop(heap)
            cur.next = lists[i]

            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
            
            cur = cur.next
        
        return head.next





        