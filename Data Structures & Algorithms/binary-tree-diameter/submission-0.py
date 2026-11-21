# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.height(root.right), self.height(root.left)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            rightHeight = self.height(root.right)
            leftHeight = self.height(root.left)
            d = rightHeight + leftHeight

        else:
            return 0

        return max(d, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))
