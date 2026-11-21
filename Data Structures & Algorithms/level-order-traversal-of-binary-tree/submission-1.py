# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = []
        res.append(root)
        
        while res:
            temp = []
            res_len = len(res)
            for i in range(res_len):
                _val = res.pop(0)
                if _val:
                    temp.append(_val.val)    
                    res.append(_val.left)
                    res.append(_val.right)

            if temp:
                q.append(temp)

        print(q)
        return q
