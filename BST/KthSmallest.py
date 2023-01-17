# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        n = 0
        # every time we pop from stack it will be the min value so we increase n
        if not root:
            return None
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            pnode = stack.pop()
            n += 1
            if n == k:
                # given n <=k so we'll definately reach this case
                return pnode.val
            curr = pnode.right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         stack = []
#
#         # do inorder traversal to get values in ascending order
#
#         if not root:
#             return None
#
#         def inorder(root):
#             if not root:
#                 return None
#             inorder(root.left)
#             stack.append(root.val)
#             inorder(root.right)
#
#         inorder(root)
#         return stack[k - 1]
