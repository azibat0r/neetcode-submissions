class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        cleaned = ""
        for j in range(len(s)):
            if (s[j].isalnum()):
                cleaned+=s[j].lower()

        for  i in range(len(cleaned)-1, -1, -1):
            if (cleaned[i].isalnum()):
                ans += cleaned[i]
        if (ans == cleaned):
            return True
        else:
            return False