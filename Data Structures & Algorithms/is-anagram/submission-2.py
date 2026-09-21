
"""
anagram
same characters,same no of times
order not important

so car and arc are anagrams

also we see regardless of order,only frequency is important = hashmap

so anagrams have what in common
same frequency of characters

so now is it possible to compare dictionaries? = yes it is

so i would iterate through s and add to a dict
then iterate through t
and compare

is len of s and t are not the same don't even bother going through the rest.

is there a better way to do this?
it is O(n+m) but m would be equal to n
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}

        for x in s:
            if x not in sdict:
                sdict[x] = 1
            else:
                sdict[x] += 1

        for x in t:
            if x not in tdict:
                tdict[x] = 1
            else:
                tdict[x] += 1

        if sdict == tdict:
            return True

        else:
            return False     





        