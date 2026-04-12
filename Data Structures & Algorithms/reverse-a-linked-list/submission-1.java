/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        //define 3 variables: prev, curr, next
        //prev null, curr head, next, head.next
        //while curr is not null
        //curr.next to prev
        //if next is null
        //break <- reached the end of the linked list and curr points to the new head
        //prev is now curr
        //curr is now next
        //next is now next.next

        if(head == null)
            return head;

        ListNode prev = null;
        ListNode curr = head;
        ListNode next;

        while(curr != null)
        {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
}
