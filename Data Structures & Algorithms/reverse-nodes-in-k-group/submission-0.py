# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        curr_tail = ListNode()
        prev_tail = None
        set_head = True
        new_head = None
        while curr is not None:
            n = 0
            prev_tail = curr_tail
            curr_tail = ListNode()
            prev = curr_tail
            curr_head = curr
            while n < k:
                if curr is None:
                    break
                prev.val = curr.val
                if k - 1 != n:
                    if curr.next is not None:
                        new_node = ListNode()
                        new_node.next = prev
                        prev = new_node
                    else:
                        print("a")
                        prev_tail.next = curr_head
                        if set_head:
                            new_head = curr_head
                            set_head = False

                        return new_head 
                curr = curr.next
                n += 1

            if set_head:
                new_head = prev
                set_head = False
            prev_tail.next = prev
        return new_head            