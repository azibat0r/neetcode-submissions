"""
so we have a fast that moves while there are 2 steps ahead
then a slow which moves normal at each step check if the fast = slow

then if it ever breaks return false



"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        if fast and fast.next and fast.next.next:
            fast = head.next
            slow = head
            while fast and fast.next and fast.next.next:
                if fast == slow:
                    return True
                fast = fast.next.next
                slow=slow.next
            return False
        else:
            return False
            
        