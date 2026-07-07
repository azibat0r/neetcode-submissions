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
        for i in range(length - 1):
            if (i + 1) == position:
                t.next = t.next.next
                break
            t = t.next
        return head