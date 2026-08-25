class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        second = set(nums)
        if len(nums) == len(second):
            return False
        else:
            return True
        