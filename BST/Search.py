# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def SearchBST(root, val):
    if not root:
        return None
    curr = root
    if curr.val == val:
        return curr
    elif val > curr.val:
        return self.searchBST(curr.right, val)
    else:
        return self.searchBST(curr.left, val)

# TC - O(logn)
