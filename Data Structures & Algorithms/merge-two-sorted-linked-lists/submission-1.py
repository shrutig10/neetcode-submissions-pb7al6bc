# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # have a loop that runs as long as both lists still has a node in it
        # create a head node (dummy node) append nodes to the end of this
        # at each iteration, compare list1 and list2
        # check that either list still has a node in it, append that whole list to the end of the linked list
        # return head.next

        head = cur = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return head.next