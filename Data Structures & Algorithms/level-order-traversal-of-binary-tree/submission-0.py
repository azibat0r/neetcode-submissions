# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        level =[]
        from collections import deque
        queue = deque()
        if not root:
            return result
        queue.append(root)
        while queue:
            length = len(queue)
            for i in range(length):
                level.append(queue[0].val)
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
            level=[]
        return result



