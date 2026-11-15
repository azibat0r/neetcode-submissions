# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
for this i am thinking at each level count one step
so let it be like the function we create would return a number

def function
while root
    return (function + 1)

or rather let the function always have 1+ to it because if it was called it means
that current node exiss

1 (1+(1+(1+0)))

2(1+(1+0))  3(1+)

4(1+0),5(1+0)

so it would be 1+ the maximum between what is returned from the function of the children


"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recursion(root):
            if not root:
                return 0
            else:
                value = 1+(max(recursion(root.left),recursion(root.right)))
                return value
        return recursion(root)
        
        
        