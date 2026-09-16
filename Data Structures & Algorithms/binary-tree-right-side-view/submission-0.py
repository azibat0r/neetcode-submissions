class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(result):
                result.append(node.val)   # first time we reach this depth
            dfs(node.right, depth + 1)    # always try right FIRST
            dfs(node.left, depth + 1)     # then left

        dfs(root, 0)
        return result