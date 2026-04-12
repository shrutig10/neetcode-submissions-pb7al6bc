# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we have to look at every node
        # checking for which is the smallest node
        # can use a min heap
        # we can store the node value along with the index of the linked list (tuple)
        
        # create min heap
        # add all of the first elements of the linked list to it
        # while there is elements in the heap, pop the top of the heap and add to a result ll
        # add the next element of that linked list to the heap (if it exists)
        # return the resulting ll

        cur = head = ListNode()
        

        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i))
        
        heapq.heapify(heap)

        while heap:
            val, idx = heapq.heappop(heap)
            cur.next = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
            cur = cur.next

        return head.next



        