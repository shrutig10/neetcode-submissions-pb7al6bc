# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # have two pointers: slow and a fast pointer
        # slow pointer goes one node at a time
        # fast pointer goes 2 nodes at a time
        # if there is a cycle, then these two are bound to meet at some point
        # if no cycle, then fast will be null 
        # fast is at the tail (fast.next.next) does not exist
        # if fast.next, else return false

        slow = fast = head

        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            
            if slow == fast:
                return True

        return False