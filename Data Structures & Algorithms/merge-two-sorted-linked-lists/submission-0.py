# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        d = ListNode()
        c = d
        a = list1
        b = list2
        while a and b :
            if (a.val<=b.val):
                d.next = a
                d = d.next
                a = a.next
            else:
                d.next = b
                d = d.next
                b = b.next  
        if a:
            d.next = a
        else:
            d.next = b
        return c.next