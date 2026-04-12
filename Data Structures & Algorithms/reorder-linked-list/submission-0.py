# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # change the tail 
        # 0 --> tail --> 0.next = 1

        # divide the list into 2
        # have a slow and fast pointer to figure out middle node
        # reverse the second half

        # merge these two lists

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        cur = slow.next
        prev = slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # prev is now head of linked list

        l2 = prev
        l1 = head
        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2




        
        