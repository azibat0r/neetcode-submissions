# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

assign a height to each node let it be 1

so in the left example
the children of 1 are of numbers
1 and 2
so we can see that 2 - 1 = 1
so if that calculation is ever 2 or more then should be false

not there is no need for the while loop if i am going to be calling the children directly

"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recursion(root):
            if not root:
                return 0

            L = recursion(root.left)
            R = recursion(root.right)

            if L is False or R is False:
                return False

            if abs(L - R) > 1:
                return False

            return 1 + max(L, R)

        return recursion(root) is not False