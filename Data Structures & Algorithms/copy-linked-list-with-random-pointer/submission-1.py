"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev = None
        new_head = prev
        old_head = head
        _data = dict()
        while old_head is not None:
            if prev is None:
                prev = Node(0)
                new_head = prev

            prev.val = old_head.val
            if old_head.next:
                prev.next = Node(0)

            _data[old_head] = prev
            prev = prev.next
            old_head = old_head.next
        
        print(_data)
        prev = new_head
        old_head = head

        while old_head is not None and prev:
            if old_head.random:
                prev.random = _data[old_head.random]

            prev = prev.next
            old_head = old_head.next

        print(_data)
        return new_head
