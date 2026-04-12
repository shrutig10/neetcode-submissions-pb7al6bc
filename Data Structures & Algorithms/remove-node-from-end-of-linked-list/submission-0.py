# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # base case: empty list
        # reverse the list, remove from beginning, reverse back
        # 2 pass approach: 1st pass used for getting the length of linked list
        # compute distance from beginning by doing length - n is the index

        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        index = length - n

        prev = None
        cur = head
        for i in range(index):
            prev = cur
            cur = cur.next
        
        if prev:
            prev.next = cur.next
        else:
            head = head.next

        return head
        