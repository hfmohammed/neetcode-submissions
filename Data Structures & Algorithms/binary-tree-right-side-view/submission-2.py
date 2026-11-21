# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = []
        q.append(root)
        while q:
            temp = []
            q_len = len(q)
            for i in range(q_len):
                n=q.pop(0)
                if n:
                    temp.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
                
            if temp:
                res.append(temp[-1])
        return res
