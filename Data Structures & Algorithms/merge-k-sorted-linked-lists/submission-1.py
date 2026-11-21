# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = ListNode()
        head = curr
        prev = None
        while True:
            _min = 1001
            _min_i = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < _min:
                    _min = lists[i].val
                    _min_i = i

            if _min_i == -1:
                if prev:
                    prev.next = None
                    break
                else:
                    return None

            curr.val = lists[_min_i].val
            curr.next = ListNode()

            prev = curr
            curr = curr.next
            lists[_min_i] = lists[_min_i].next
        return head
