"""
s1 = "abc", s2 = "lecabee"

abc

lecabee
  abc

what do cab and abc have in common
set(cab) = set(abc)

lecabee
  l r

set = lec
remove l and add a
set = eca
remove e and add b
set = cab

so 2 sets
set of s1
set for s2

while r < len of s2
build a window which is length of s1
    add all in window to set for s2
left pointer at beginning of window
right pointer at end of window

push each forward if window set is not equal to s1 set

if it ends return false

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d = {}
        s2_d = {}

        for char in s1:
            if char not in s1_d:
                s1_d[char] = 1
            else:
                s1_d[char] += 1
        
        if len(s2)<len(s1):
            return False
        
        for i in range(len(s1)):
            if s2[i] not in s2_d:
                s2_d[s2[i]] = 1
            else:
                s2_d[s2[i]] +=1
        l = 0
        r = len(s1)-1

        while r < len(s2):
            if s1_d == s2_d:
                return True
            else:
                s2_d[s2[l]]-=1
                if s2_d[s2[l]] < 1:
                    del s2_d[s2[l]]
                l+=1
                r+=1
                if r >= len(s2): break

                if s2[r] not in s2_d:
                    s2_d[s2[r]] = 1
                else:
                    s2_d[s2[r]] += 1
                print(s2_d)
        return False
        


        