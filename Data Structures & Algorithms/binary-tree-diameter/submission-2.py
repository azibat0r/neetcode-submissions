# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
is kind of like the last one 
but the addition of the number of children it has

1 (0L 3R) so a total of 3 paths we are saving the 1 + max(number of children it has)

   2 (2Left 1 right) so a total of 3
 
   3 4
5

so your intution was correct but what i lack understanding is the recursion part


the return 1 + max .. reps what the recursion(would return)
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.val = 0
        def recursion(root):
            if not root:
                return 0
            else:
                left = recursion(root.left)
                right = recursion(root.right)

                self.val = max(self.val, left + right)

                return 1 + max(recursion(root.left),recursion(root.right))
        recursion(root)
        return self.val