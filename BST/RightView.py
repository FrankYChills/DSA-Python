# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightestNodes = []

        def bfs(root):
            if not root:
                return None
            levelnodes = []
            q = deque()
            q.append(root)
            while q:
                for i in range(len(q)):
                    remNode = q.popleft()
                    if remNode.left:
                        q.append(remNode.left)
                    if remNode.right:
                        q.append(remNode.right)
                    levelnodes.append(remNode.val)
                    # append the last child/rightest
                rightestNodes.append(levelnodes[-1])

        bfs(root)
        return rightestNodes