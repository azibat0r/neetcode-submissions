
"""BaseCase if path same size as nums
    Constraint if number picked already in path dont add
    Action (Append)
    Backtrack
    Pop"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def repeat(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for a in nums:
                if a in path:
                    continue
                else:
                    path.append(a)
                    repeat(path)
                    path.pop()
        repeat(path)
        return result
                