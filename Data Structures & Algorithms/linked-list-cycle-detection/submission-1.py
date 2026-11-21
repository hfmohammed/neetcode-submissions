# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        s = head
        f = head.next

        while s != f:
            if s is None or f is None:
                return False
            
            s = s.next
            f = f.next
            if f is not None:
                f = f.next
            else:
                return False
        
        return True
