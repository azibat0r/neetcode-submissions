class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: # if nums is empty or , if len(nums) == 0
            return 0
        counter = 1
        longest = 1
        a = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and a[i] == a[i-1]: #solves the duplicate issue
                continue
            if a[i]+1 in a:
                counter += 1
            else:
                if counter > longest:
                    longest = counter
                counter = 1
        if longest > counter: #note this only happends after the OG loop ends
            return longest
        else:
            return counter