"""
s = "zxyzxyz"

zxy z is in set

zxyzxyz
 l  r

while r < len:
which if r is in set
    yes
    l.remove
    l+=1
    distance = max(distance, l-r+1)

    no
    add r to set
    r+=1
    distance = max(distance, l-r+1)
  
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distance = 1
        l = 0
        r = 0
        a = set()
        if not s:
            return 0

        while r < len(s):
            if s[r] not in a:
                a.add(s[r])
                distance = max(distance,r-l+1)
                r+=1
            else:
                a.remove(s[l])
                l+=1
                distance = max(distance,r-l+1)

        return distance


"""
abcabcbb
l
  r
distance = 3
(abc)





"zxyzxyz"
   l
     r
d = 3
(yzx)




"xxxx"
  l
   r
distance = 1

(x)


"""
