class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        b = set()
        length = 0
        while r < len(s):
            if s[r] not in b:
                b.add(s[r])
                r+=1
                length = max(r-l, length)
            else:
                b.remove(s[l])
                l+=1
        return length

