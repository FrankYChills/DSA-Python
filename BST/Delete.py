# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getMin(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # edge case
        if not root:
            return None

        curr = root
        if key < curr.val:
            curr.left = self.deleteNode(curr.left, key)
        elif key > curr.val:
            curr.right = self.deleteNode(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            # node has two childrens
            # find min from right node
            minNode = self.getMin(curr.right)
            # swap with root node
            curr.val = minNode.val
            # remove minNode from right tree
            curr.right = self.deleteNode(curr.right, minNode.val)

        return curr

#TC - O(logn)