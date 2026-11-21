# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = None
        curr = head
        new_head = None
        prev_tail = None
        fast = head
        while curr is not None:
            # use fast pointer to check for a full group
            for _ in range(k):
                print(_)
                if fast is not None:
                    fast = fast.next
                else:
                    if prev_tail:
                        prev_tail.next = curr
                    else:
                        new_head = head
                    return new_head
            
            new_tail = None
            n = 0
            while n < k:
                if new_tail is None:
                    new_tail = curr

                # reverse the values
                _next = curr.next
                curr.next = prev
                prev = curr
                curr = _next

                n += 1

            if new_head is None:
                # first iter
                new_head = prev
            else:
                prev_tail.next = prev
                new_tail.next = None
            prev_tail = new_tail

        return new_head

