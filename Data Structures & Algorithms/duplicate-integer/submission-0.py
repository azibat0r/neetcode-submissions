class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        b = set(nums)
        c = len(b)
        if (a == c):
            return False
        else :
            return True
        
