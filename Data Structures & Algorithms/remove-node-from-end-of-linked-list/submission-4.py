"""
[1,2,3,4]
     2

n = 2

2nd from the end when length is 4 is 4-(2-1) = 3rd node

so find length through iterating

then when found
stop at the node before it
if next.next exist
then that node.next = next.next

lets see if it would be an issue that the removed is still connected


"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        a = head
        while a:
            length +=1
            a = a.next
        print(length)
        remove = length - (n-1)
        print(remove)

        a = head
        prev = None
        count = 0
        while a:
            count += 1
            if count == length and length == 1:
                a.val = None
                return 
            if count == remove:
                if prev == None:
                    head = head.next
                    a.next = None
                    return head
                prev.next = prev.next.next
                a.next = None
                return head
            prev = a
            a = a.next
        return head


        