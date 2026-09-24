"""
Input: s = "zxyzxyz"

Output: 3


"zxyzxyz"
i
j j j j

set(zxy)
i remove z then move +=1
until = j
then j adds and so forth

abaecd
aecdab

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        a = set()
        counter = 0
        current = 0
        if len(s) == 0:
            return 0

        while j < len(s):
            if s[j] not in a:
                a.add(s[j])
                current += 1
                j+=1
                counter = max(current,counter)

            else:
                counter = max(current,counter)
                while s[j] in a:
                    a.remove(s[i])
                    i+=1
                current = j - i

        return counter


                

        