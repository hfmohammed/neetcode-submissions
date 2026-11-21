# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = l1
        carry = 0
        prev = None
        while l2 or l1 or carry:
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0

            temp = l1_val + l2_val + carry
            print(temp, l1_val, l2_val, carry)

            if l1:
                l1.val = temp % 10
                prev = l1
            else:
                prev.next = ListNode(temp % 10, None)
                prev = prev.next


            carry = temp // 10

            if l2:
                l2 = l2.next

            if l1:
                l1 = l1.next
        
        return res
