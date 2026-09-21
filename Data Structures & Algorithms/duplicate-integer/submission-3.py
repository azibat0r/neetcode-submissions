"""
sets do not allow for duplicates to be contained
compare the length of the list and the set

"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = len(nums)
        a = set()

        for x in nums:
            a.add(x)
        count = len(a)

        if count != num:
            return True
        else:
            return False