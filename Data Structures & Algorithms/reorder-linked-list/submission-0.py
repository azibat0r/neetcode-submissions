# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        secondhead = slow.next
        slow.next = None

        prev = None
        while secondhead:
            save = secondhead.next 
            secondhead.next = prev
            prev = secondhead
            secondhead = save

        
        first = head
        second = prev
        while first and second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
