# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        s.append(root)
        res = []
        while s:
            if not root:
                node = s.pop()
                if node:
                    res.append(node.val)
                    root = node.right
                    s.append(root)
            else:
                root = root.left
                s.append(root)
            
        print(res)
        return res[k - 1]
