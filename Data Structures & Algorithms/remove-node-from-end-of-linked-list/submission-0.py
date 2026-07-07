# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        count = head
        while count:
            count = count.next
            length += 1
        position = length - n
        if position == 0:
            return head.next
        t = head
        p = None
        for i in range(position):
            p = t
            t = t.next
        a = t.next
        t.next = None
        p.next = a

        return head
