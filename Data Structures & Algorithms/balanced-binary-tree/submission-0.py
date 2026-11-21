# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.right), self.height(root.left)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            rightHeight = 0
        else:
            rightHeight = self.height(root.right)

        if root is None:
            leftHeight = 0
        else:
            leftHeight = self.height(root.left)

        if not rightHeight and not leftHeight:
            return True
        return self.isBalanced(root.right) and self.isBalanced(root.left) and abs(rightHeight - leftHeight) <= 1
