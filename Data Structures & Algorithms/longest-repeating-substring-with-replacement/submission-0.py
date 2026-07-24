class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        result = 0
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            replacements = (r - l + 1) - max(freq.values())
            if replacements > k:
                freq[s[l]] -= 1
                l += 1
            else:
                result = max(r-l+1, result)
        return result
