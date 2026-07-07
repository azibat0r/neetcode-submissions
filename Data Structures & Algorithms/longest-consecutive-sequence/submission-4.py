class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counter = 1
        longest = 1
        a = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and a[i] == a[i-1]:
                continue
            if a[i]+1 in a:
                counter += 1
            else:
                if counter > longest:
                    longest = counter
                counter = 1
        if longest > counter:
            return longest
        else:
            return counter