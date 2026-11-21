# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        l = head
        r = head

        while n:
            r = r.next
            n -= 1
        
        while r is not None:
            r = r.next
            prev = head
            head = head.next
        
        print(head.val)
        if prev:
            prev.next = head.next
            print(head.next)
        else:
            head = head.next
            prev = head
            l = prev
        return l
