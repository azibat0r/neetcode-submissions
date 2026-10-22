"""
create a set that stores the numbers and check as you iterate whether it is alreeady in the set



"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = set()

        for char in nums:
            if char in a:
                return char
            else:
                a.add(char)
        
        