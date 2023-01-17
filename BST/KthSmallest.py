# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        # do inorder traversal to get values in ascending order

        if not root:
            return None

        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            stack.append(root.val)
            inorder(root.right)

        inorder(root)
        return stack[k - 1]
