# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        queue = deque([root])
        res = deque()
        while queue:
            for _ in range(len(queue)):
                item = queue.popleft()
                res.append(str(item.val) if item else "null")

                if item:
                    queue.append(item.left)
                    queue.append(item.right)
        
        while res and res[-1] == "null":
            res.pop()
        
        return ",".join(res)


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")
        if data[0] == "null":
            return None

        l = deque(data)

        root = TreeNode(int(l[0]))
        queue = deque([root])

        curr = 1
        while queue and curr < len(l):
            node = queue.popleft()

            if curr < len(l) and l[curr] != "null":
                node.left = TreeNode(int(l[curr]))
                queue.append(node.left)
            curr += 1

            if curr < len(l) and l[curr] != "null":
                node.right = TreeNode(int(l[curr]))
                queue.append(node.right)
            curr += 1
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))