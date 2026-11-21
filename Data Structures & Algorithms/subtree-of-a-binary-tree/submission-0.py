# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, p, q):
        if not (p and q):
            return not p and not q

        return p.val == q.val and self.isSame(p.right, q.right) and self.isSame(p.left, q.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSame(root, subRoot):
            return True
        
        if root is None:
            return False

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)