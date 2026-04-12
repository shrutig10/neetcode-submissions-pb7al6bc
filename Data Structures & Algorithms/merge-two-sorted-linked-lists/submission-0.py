# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a separate merged linked list
        # loop through both lists at the same time
        # whichever list has the lesser element, append that to our merged linked list
        # will need a list1 and list2 pointer (given in header)
        # once we hit the end of one list, append the rest of the elements from the other list to the merged linked list
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
