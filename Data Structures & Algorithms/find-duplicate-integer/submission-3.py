class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
            if count[i] >= 2:
                return i
        