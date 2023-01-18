# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        allnodes = []

        def bfs(root):
            level = 1
            lnodes = []
            curQueue = deque()
            if not root:
                return
            curQueue.append(root)
            while curQueue:
                for i in range(len(curQueue)):
                    remNode = curQueue.popleft()
                    if remNode.left:
                        curQueue.append(remNode.left)
                    if remNode.right:
                        curQueue.append(remNode.right)
                    lnodes.append(remNode.val)
                level += 1
                allnodes.append(lnodes)
                lnodes = []

        bfs(root)
        return allnodes
