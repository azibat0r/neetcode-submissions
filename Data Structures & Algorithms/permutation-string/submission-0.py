class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        a1 = {}
        a2 = {}

        for x in s1:
            a1[x] = a1.get(x, 0) + 1

        left = 0
        right = len(s1) - 1
        for i in range(left, right + 1):
            a2[s2[i]] = a2.get(s2[i], 0) + 1

        if a1 == a2:
            return True

        while right < len(s2) - 1:
            a2[s2[left]] -= 1
            if a2[s2[left]] == 0:
                del a2[s2[left]]
            left += 1
            right += 1
            a2[s2[right]] = a2.get(s2[right], 0) + 1

            if a1 == a2:
                return True

        return False
